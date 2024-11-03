from fastapi import HTTPException
import PyPDF2
import json
import os
from models.input_models import PDFInput
from services.ai_service import AIService
from services.presentation_service import PresentationService


class PresentationController:
    def __init__(self):
        self.ai_service = AIService()
        self.presentation_service = PresentationService()

    async def generate_presentation(self, pdf_input: PDFInput):
        try:
            if not os.path.isfile(pdf_input.pdf_path):
                raise HTTPException(
                    status_code=404,
                    detail=f"PDF dosyası bulunamadı: {pdf_input.pdf_path}"
                )

            # PDF'den metin çıkar
            with open(pdf_input.pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ' '.join(page.extract_text() for page in reader.pages)

            # Gemini ile içerik oluştur
            try:
                response = self.ai_service.generate_content(text)
                content = json.loads(response.text)
            except json.JSONDecodeError as e:
                print(f"JSON parse hatası: {str(e)}")
                print(f"AI yanıtı: {response.text}")
                # JSON yanıtını temizle
                cleaned_response = response.text.strip()
                if '```json' in cleaned_response:
                    cleaned_response = cleaned_response.split('```json')[1].split('```')[0]
                content = json.loads(cleaned_response)
            except Exception as e:
                print(f"AI yanıt hatası: {str(e)}")
                raise HTTPException(
                    status_code=500,
                    detail=f"AI yanıtı işlenirken hata oluştu: {str(e)}"
                )

            # Çıktı dizini oluştur
            output_dir = pdf_input.output_dir or os.path.dirname(pdf_input.pdf_path)
            os.makedirs(output_dir, exist_ok=True)

            # Sunum oluştur
            presentation_path = self.presentation_service.create_pptx(content, output_dir)

            return {
                "message": "Sunum başarıyla oluşturuldu",
                "file_path": presentation_path
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Sunumu oluşturma hatası: {str(e)}"
            )

