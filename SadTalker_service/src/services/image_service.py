from PIL import Image
import io
import os
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from services.chrome_service import ChromeService

class ImageService:
    @staticmethod
    def convert_to_supported_format(image_data):
        try:
            image = Image.open(io.BytesIO(image_data))
            output = io.BytesIO()
            image = image.convert('RGB')
            image.save(output, format='PNG')
            return output.getvalue()
        except Exception as e:
            print(f"Görüntü dönüştürme hatası: {str(e)}")
            return None

    @staticmethod
    def download_image(keyword: str, download_path: str) -> str | None:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        file_path = os.path.join(download_path, f"{keyword}.png")

        if os.path.exists(file_path):
            return file_path

        driver = None
        try:
            driver = ChromeService.initialize_driver()
            if not driver:
                raise Exception("WebDriver başlatılamadı")

            driver.get("https://images.google.com")

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(f"{keyword} transparent background")
            search_box.send_keys(Keys.RETURN)

            time.sleep(2)

            img_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".rg_i"))
            )

            img_url = img_element.get_attribute('srcq') or img_element.get_attribute('data-srcq')

            if img_url:
                response = requests.get(img_url, timeout=10)
                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    return file_path

            return None

        except Exception as e:
            print(f"Görsel indirme hatası: {e}")
            return None

        finally:
            if driver:
                driver.quit()
