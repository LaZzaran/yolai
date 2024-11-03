from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.models import Answer
from app.gemini_service import GeminiService
from app.session_manager import SessionManager

GEMINI_API_KEY = "API_KEY_BURAYA_GIR"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.gemini_service = GeminiService(api_key=GEMINI_API_KEY)
    app.state.session_manager = SessionManager()
    yield
    app.state.session_manager = SessionManager()


app = FastAPI(
    title="Career Counselor API",
    description="Kariyer danışmanlığı API'si",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Kariyer Danışmanlığı API'sine Hoş Geldiniz",
        "version": "1.0.0",
        "endpoints": {
            "current-question": "/current-question",
            "submit-answer": "/submit-answer",
            "progress": "/progress",
            "reset": "/reset"
        }
    }


@app.get("/current-question")
async def get_current_question(app_state: dict = Depends(lambda: app.state)):
    response = app_state.session_manager.get_current_question()
    return JSONResponse(
        content=response,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )


@app.post("/submit-answer")
async def submit_answer(
        answer: Answer,
        app_state: dict = Depends(lambda: app.state)
):
    response = app_state.session_manager.submit_answer(answer.answer)

    if response is None:  # All questions completed
        analysis = await app_state.gemini_service.analyze_answers(
            app_state.session_manager.get_answers()
        )
        return JSONResponse(
            content={
                "status": "completed",
                "message": "Tüm sorular tamamlandı",
                "analysis": analysis
            },
            headers={"Content-Type": "application/json; charset=utf-8"}
        )

    return JSONResponse(
        content=response,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )


@app.get("/progress")
async def get_progress(app_state: dict = Depends(lambda: app.state)):
    response = app_state.session_manager.get_progress()
    return JSONResponse(
        content=response,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )


@app.post("/reset")
async def reset_session(app_state: dict = Depends(lambda: app.state)):
    app_state.session_manager.reset()
    return JSONResponse(
        content={"status": "success", "message": "Oturum sıfırlandı"},
        headers={"Content-Type": "application/json; charset=utf-8"}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)