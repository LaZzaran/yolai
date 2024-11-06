from pdf_extractor import PDFExtractor
from slide_content_generator import SlideContentGenerator
from image_downloader import ImageDownloader
from presentation_creator import PresentationCreator

class PresentationManager:
    def __init__(self, api_key):
        self.pdf_extractor = PDFExtractor()
        self.slide_content_generator = SlideContentGenerator(api_key)
        self.image_downloader = ImageDownloader()
        self.presentation_creator = PresentationCreator()

    def create_presentation(self, pdf_file):
        text = self.pdf_extractor.extract_text_from_pdf(pdf_file)
        slides_data = self.slide_content_generator.get_presentation_content(text)

        for slide in slides_data['slides']:
            if 'image_keyword' in slide:
                search_term = slide['image_keyword']['search_term']
                self.image_downloader.download_image(search_term)

        output_file = self.presentation_creator.create_pptx(slides_data)
        return output_file

if __name__ == "__main__":
    GOOGLE_API_KEY = 'Your_google_apikey'
    pdf_file = "SindirimSistemi.pdf"
    manager = PresentationManager(GOOGLE_API_KEY)
    result = manager.create_presentation(pdf_file)
    print(f"Sunum başarıyla oluşturuldu: {result}")
