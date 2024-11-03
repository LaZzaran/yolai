from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from exceptions import TimeoutException

class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def open_google_images(self):
        self.driver.get("https://www.google.com/imghp")
        print("Google Görseller sayfası açıldı")
        time.sleep(2)

    def search_images(self, keyword):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        print(f"'{keyword}' için arama yapıldı")
        time.sleep(3)

    def find_thumbnails(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.VgUlZ-KoEcSF7NYPy56j2Ao_6"))
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def click_thumbnail_and_get_image_url(self, thumbnail):
        self.driver.execute_script("arguments[0].click();", thumbnail)
        time.sleep(2)
        large_image = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'source_image[jsname="kn3ccd"]'))
        )
        return large_image.get_attribute('src')

    def quit(self):
        self.driver.quit()
