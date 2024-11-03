import os
import requests
import time
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from exceptions import TimeoutException, ImageDownloadException


class ImageDownloader:
    def __init__(self, keyword, download_path, num_images=5):
        self.keyword = keyword
        self.download_path = download_path
        self.num_images = num_images
        self.browser = Browser()

    def download_images(self):
        downloaded = 0
        self._prepare_directory()

        try:
            self.browser.open_google_images()
            self.browser.search_images(self.keyword)

            thumbnails = self.browser.find_thumbnails()

            for i, thumbnail in enumerate(thumbnails[:self.num_images]):
                try:
                    self.browser.scroll_to_element(thumbnail)
                    img_url = self.browser.click_thumbnail_and_get_image_url(thumbnail)

                    if img_url:
                        self._download_image(img_url, downloaded + 1)
                        downloaded += 1

                        if downloaded >= self.num_images:
                            print("İstenilen sayıda resim indirildi!")
                            break
                except ImageDownloadException as e:
                    print(f"Resim indirirken hata oluştu: {str(e)}")
                    continue

        except TimeoutException as e:
            print(f"Genel hata: {str(e)}")

        finally:
            self.browser.quit()
            return downloaded

    def _prepare_directory(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def _download_image(self, url, image_num):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                file_path = os.path.join(self.download_path, f"{self.keyword}_{image_num}.jpg")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"İndirildi: {file_path}")
            else:
                raise ImageDownloadException("Resim indirilemedi.")
        except requests.RequestException as e:
            print(f"İndirme sırasında hata oluştu: {str(e)}")