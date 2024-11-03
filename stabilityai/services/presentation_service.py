from pdf_service import extract_text_from_pdf
from prompt_service import get_presentation_content
from stabilityai.utils.pptx_utils import create_pptx
from stabilityai.config import OUTPUT_PRESENTATION_DIR
from pathlib import Path

def create_presentation(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    slides_data = get_presentation_content(text)
    output_file = f"{OUTPUT_PRESENTATION_DIR}/{Path(pdf_file).stem}_presentation.pptx"
    create_pptx(slides_data, output_file)
    return output_file
