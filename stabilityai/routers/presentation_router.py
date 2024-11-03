from fastapi import APIRouter, HTTPException
from stabilityai.services.presentation_service import create_presentation
from pydantic import BaseModel
import os

class PDFInput(BaseModel):
    pdf_path: str

router = APIRouter()

@router.post("/create-presentation")
async def generate_presentation(pdf_input: PDFInput):
    pdf_path = pdf_input.pdf_path
    if not os.path.isfile(pdf_path):
        raise HTTPException(status_code=404, detail="PDF dosyası bulunamadı")
    try:
        result_file = create_presentation(pdf_path)
        return {"message": "Sunum başarıyla oluşturuldu", "file_path": result_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata oluştu: {str(e)}")