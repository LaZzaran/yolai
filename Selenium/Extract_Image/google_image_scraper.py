from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from typing import Optional


class GoogleImageScraper:
    """
    Google görsellerinden resim div'lerini yakalayan sınıf
    """

    def __init__(self, screenshot_path: str):
        """
        Args:
            screenshot_path (str): Ekran görüntülerinin kaydedileceği dizin
        """
        self.screenshot_path = screenshot_path
        self.driver: Optional[webdriver.Chrome] = None
        self._setup_screenshot_directory()

    def _setup_screenshot_directory(self) -> None:
        """Screenshot dizinini oluşturur"""
        if not os.path.exists(self.screenshot_path):
            os.makedirs(self.screenshot_path)

    def _initialize_driver(self) -> None:
        """Selenium web driver'ı başlatır"""
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def _navigate_to_google_images(self) -> None:
        """Google Görseller sayfasına gider"""
        self.driver.get("https://www.google.com/imghp")
        time.sleep(2)

    def _search_keyword(self, keyword: str) -> None:
        """
        Verilen anahtar kelimeyi arar

        Args:
            keyword (str): Aranacak kelime
        """
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def _scroll_to_top(self) -> None:
        """Sayfayı en üste kaydırır"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

    def _find_thumbnails(self) -> list:
        """
        Resim div'lerini bulur

        Returns:
            list: Bulunan div elementlerinin listesi
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.H8Rx8c"))
        )

    def _capture_thumbnail(self, thumbnail, keyword: str, index: int) -> bool:
        """
        Belirtilen thumbnail'in ekran görüntüsünü alır

        Args:
            thumbnail: Ekran görüntüsü alınacak element
            keyword (str): Arama kelimesi
            index (int): Görüntü indeksi

        Returns:
            bool: İşlem başarılı ise True
        """
        try:
            self.driver.execute_script("""
                arguments[0].scrollIntoView();
                window.scrollBy(0, -150);
            """, thumbnail)
            time.sleep(1)

            screenshot_path = os.path.join(
                self.screenshot_path,
                f"{keyword}_div_{index + 1}.png"
            )
            thumbnail.screenshot(screenshot_path)
            print(f"Ekran görüntüsü alındı: {screenshot_path}")
            return True
        except Exception as e:
            print(f"Thumbnail yakalama hatası: {str(e)}")
            return False

    def capture_images(self, keyword: str, num_images: int = 5) -> int:
        """
        Verilen anahtar kelime için Google'dan görsel divlerinin
        ekran görüntüsünü alır

        Args:
            keyword (str): Aranacak kelime
            num_images (int): Alınacak görüntü sayısı

        Returns:
            int: Başarıyla alınan ekran görüntüsü sayısı
        """
        captured = 0

        try:
            self._initialize_driver()
            self._navigate_to_google_images()
            print("Google Görseller sayfası açıldı")

            self._search_keyword(keyword)
            print(f"'{keyword}' için arama yapıldı")

            self._scroll_to_top()
            print("Resimler aranıyor...")

            thumbnails = self._find_thumbnails()
            print(f"Resimler bulundu. İlk {num_images} tanesinin ekran görüntüsü alınacak.")

            for i, thumbnail in enumerate(thumbnails[:num_images]):
                if self._capture_thumbnail(thumbnail, keyword, i):
                    captured += 1

                if captured >= num_images:
                    print("İstenilen sayıda ekran görüntüsü alındı!")
                    break

        except Exception as e:
            print(f"Genel hata: {str(e)}")

        finally:
            if self.driver:
                self.driver.quit()

        print(f"İşlem tamamlandı. {captured} ekran görüntüsü alındı.")
        return captured

    def __del__(self):
        """Sınıf yok edilirken driver'ı kapatır"""
        if self.driver:
            self.driver.quit()