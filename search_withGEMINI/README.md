# Eğitim Asistanı API

Bu proje, öğrencilere sorularını yanıtlamada yardımcı olan bir eğitim asistanı API'sidir. Google Generative AI kullanarak sorulara yanıt verir.

## Kurulum

1. Bu projeyi klonlayın:
    ```bash
    git clone https://github.com/kullanici_adiniz/egitim-asistani-api.git
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
## API Uç Noktaları
1. **GET** /: Ana sayfa, API'ye hoş geldiniz mesajı döner.
2. **POST /ask**: Soruları alır ve yanıt verir. Gövde verisi question adlı bir metin alanı içermelidir.

## Çalıştırma

Aşağıdaki komut ile projeyi çalıştırabilirsiniz:
```bash

uvicorn main:app --reload --port 8001

curl -X POST "http://localhost:8001/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "Maddenin Halleri konusunu bana anlatır mısın?"}'