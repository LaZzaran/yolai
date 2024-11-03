import google.generativeai as genai
import os
import requests
from PIL import Image
from datetime import datetime


def setup_gemini(api_key):
    """
    Gemini API'yi yapılandırır
    """
    genai.configure(api_key=api_key)


def generate_and_save_image(prompt, save_dir="generated_images"):
    """
    Verilen prompt'a göre görsel oluşturur ve kaydeder

    Args:
        prompt (str): Görsel oluşturmak için kullanılacak açıklama
        save_dir (str): Görsellerin kaydedileceği dizin

    Returns:
        str: Kaydedilen dosyanın yolu
    """
    try:
        # Gemini model instance'ını oluştur
        model = genai.GenerativeModel('gemini-pro-vision')

        # Görsel oluştur
        response = model.generate_image(
            prompt=prompt,
            size='1024x1024'  # Görsel boyutu
        )

        # Dizin yoksa oluştur
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Dosya adını oluştur (timestamp ile benzersiz olmasını sağla)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_image_{timestamp}.png"
        filepath = os.path.join(save_dir, filename)

        # Görseli kaydet
        with open(filepath, 'wb') as f:
            f.write(response.image)

        print(f"Görsel başarıyla kaydedildi: {filepath}")
        return filepath

    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return None


# Kullanım örneği
if __name__ == "__main__":
    # API anahtarını buraya girin
    GEMINI_API_KEY = "AIzaSyAT8sDfuOOwSbl_3_8KZoWdZQgyKI-XWJA"

    # API'yi yapılandır
    setup_gemini(GEMINI_API_KEY)

    # Örnek prompt
    prompt = "a beautiful sunset over mountains with a lake in the foreground"

    # Görsel oluştur ve kaydet
    generated_image_path = generate_and_save_image(prompt)

    if generated_image_path:
        print(f"İşlem başarılı! Görsel şurada: {generated_image_path}")
    else:
        print("Görsel oluşturma başarısız oldu.")