'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def capture_image_divs(keyword, screenshot_path, num_images=5):
    """
    Verilen anahtar kelime için Google'dan görsel divlerinin ekran görüntüsünü alır
    """
    captured = 0

    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        # Google Görseller'e git
        driver.get("https://www.google.com/imghp")
        print("Google Görseller sayfası açıldı")
        time.sleep(2)

        # Arama yap
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        print(f"'{keyword}' için arama yapıldı")
        time.sleep(3)

        # Sayfayı en üste scroll yap
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        print("Resimler aranıyor...")

        # Yeni class seçicisi ile resimleri bul
        thumbnails = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.H8Rx8c"))
        )

        print(f"Resimler bulundu. İlk {num_images} tanesinin ekran görüntüsü alınacak.")

        # Sadece ilk 5 div için işlem yap
        for i, thumbnail in enumerate(thumbnails[:num_images]):
            try:
                # Div'i görünür yap ve biraz yukarıda tut
                driver.execute_script("""
                    arguments[0].scrollIntoView();
                    window.scrollBy(0, -150);
                """, thumbnail)
                time.sleep(1)

                # Div'in ekran görüntüsünü al
                screenshot_path_file = os.path.join(screenshot_path, f"{keyword}_div_{captured + 1}.png")
                thumbnail.screenshot(screenshot_path_file)
                print(f"Ekran görüntüsü alındı: {screenshot_path_file}")
                captured += 1

                if captured >= num_images:
                    print("İstenilen sayıda ekran görüntüsü alındı!")
                    break

            except Exception as e:
                print(f"Hata: {str(e)}")
                continue

    except Exception as e:
        print(f"Genel hata: {str(e)}")

    finally:
        print(f"İşlem tamamlandı. {captured} ekran görüntüsü alındı.")
        driver.quit()
        return captured

# Kullanım örneği
if __name__ == "__main__":
    keyword = "dolaşım sistemi"  # Aranacak kelime
    screenshot_path = "../../screenshots"  # Ekran görüntülerinin kaydedileceği klasör
    total_captured = capture_image_divs(keyword, screenshot_path)
    print(f"Toplam {total_captured} ekran görüntüsü başarıyla alındı.")'''