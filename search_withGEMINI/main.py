from fastapi import FastAPI, HTTPException
from models import QuestionRequest
from generator import ContentGenerator

app = FastAPI()
content_generator = ContentGenerator()

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        response = content_generator.generate(request.question)
        return {"answer": response}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/")
async def root():
    return {"message": "Eğitim Asistanı API'sine Hoş Geldiniz"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
