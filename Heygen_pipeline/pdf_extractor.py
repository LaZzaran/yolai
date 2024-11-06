import PyPDF2

class PDFExtractor:
    @staticmethod
    def extract_text_from_pdf(pdf_file):
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text
