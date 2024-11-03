from fastapi import FastAPI, File, UploadFile, HTTPException
from services.pdf_service import PDFService
from services.quiz_service import QuizService
from models import SinavCevap

app = FastAPI(title="PDF Sınav Oluşturucu API")
quiz_service = QuizService()
pdf_service = PDFService()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")

    text_content = await pdf_service.extract_text(file)
    quiz_data = await quiz_service.create_quiz(text_content)
    return {"sorular": quiz_data["questions"]}

@app.post("/submit-answers/")
async def submit_answers(quiz_answers: SinavCevap):
    return quiz_service.grade_quiz(quiz_answers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)