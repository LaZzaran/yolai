from google_image_scraper import GoogleImageScraper
from config import Config


def main():
    # Scraper örneği oluştur
    scraper = GoogleImageScraper(Config.DEFAULT_SCREENSHOT_PATH)

    # Aranacak kelime
    keyword = "dolaşım sistemi"

    # Görüntüleri yakala
    total_captured = scraper.capture_images(
        keyword=keyword,
        num_images=Config.DEFAULT_NUM_IMAGES
    )

    print(f"Toplam {total_captured} ekran görüntüsü başarıyla alındı.")


if __name__ == "__main__":
    main()