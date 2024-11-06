import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImageDownloader:
    def __init__(self, download_path='downloaded_images'):
        self.download_path = download_path
        os.makedirs(download_path, exist_ok=True)

    def download_image(self, keyword):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        try:
            driver.get("https://www.google.com/imghp")
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)

            thumbnail = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.H8Rx8c"))
            )
            img_element = thumbnail.find_element(By.TAG_NAME, "img")
            driver.execute_script("arguments[0].click();", img_element)
            time.sleep(2)

            large_image = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'img[jsname="kn3ccd"]'))
            )
            img_url = large_image.get_attribute('src')

            if img_url and img_url.startswith('http'):
                response = requests.get(img_url, timeout=10, verify=False)
                if response.status_code == 200:
                    file_path = os.path.join(self.download_path, f"{keyword}.jpg")
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    return file_path
        finally:
            driver.quit()
