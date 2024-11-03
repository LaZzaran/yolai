import os
from fastapi import HTTPException, UploadFile
from pypdf import PdfReader

class PDFService:
    @staticmethod
    async def extract_text(pdf_file: UploadFile) -> str:
        temp_path = f"temp_{pdf_file.filename}"
        try:
            with open(temp_path, "wb") as f:
                content = await pdf_file.read()
                f.write(content)

            reader = PdfReader(temp_path)
            text_content = []

            for page in reader.pages:
                text = page.extract_text()
                text = " ".join(text.split())
                if text.strip():
                    text_content.append(text)

            return " ".join(text_content)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"PDF processing error: {str(e)}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)