from fastapi import FastAPI, Request, HTTPException
from controllers.presentation_controller import PresentationController
from services.sadtalker_service import SadTalkerService
from models.input_models import PDFInput

app = FastAPI()
presentation_controller = PresentationController()
sadtalker_service = SadTalkerService()


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return {
        "status": "error",
        "message": str(exc),
        "type": type(exc).__name__
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return {
        "status": "error",
        "message": exc.detail,
        "status_code": exc.status_code
    }


@app.on_event("startup")
async def startup_event():
    """Uygulama başlangıcında SadTalker kurulumunu yap"""
    try:
        sadtalker_service.setup()
    except Exception as e:
        print(f"SadTalker kurulum hatası: {str(e)}")
        # Kurulum hatası olsa bile uygulamanın çalışmasına izin ver
        pass


@app.post("/create-presentation")
async def generate_presentation(pdf_input: PDFInput):
    return await presentation_controller.generate_presentation(pdf_input)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)