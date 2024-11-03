from pydantic import BaseModel

class PDFInput(BaseModel):
    pdf_path: str
    output_dir: str | None = None