#### Önemli Not: Bu bölüm, yüksek donanım gereksinimleri sebebiyle yarışma sürecinde geçici olarak askıya alınmıştır.

# Sunum Oluşturma API'si

Bu proje, verilen bir PDF dosyasındaki metni analiz ederek profesyonel bir sunum oluşturmak için tasarlanmış bir FastAPI uygulamasıdır. Proje, metin içeriğine göre görsel arama terimleri üreten ve bu terimleri kullanarak AI tabanlı görüntü oluşturma işlevi ile desteklenmiş bir sunum dosyası (.pptx) üretir. Proje, Hugging Face ve Google API gibi çeşitli üçüncü parti hizmetleri kullanır.

## Özellikler

- **PDF İçeriği Analizi**: PDF dosyasındaki metni okuyarak belirli kurallar çerçevesinde sunum slaytları oluşturur.
- **Görsel Arama Terimi Üretimi**: Her slayt için uygun bir görsel arama terimi belirler.
- **AI Tabanlı Görsel Oluşturma**: Hugging Face üzerinden metne uygun AI tabanlı görseller oluşturur.
- **Sunum Dosyası Oluşturma**: Üretilen slaytları ve görselleri kullanarak bir PowerPoint dosyası (pptx) hazırlar.

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. **Projeyi klonlayın**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2. **Gereksinimleri yükleyin**:
    ```bash
   pip install -r requirements.txt

3. **Ortam Değişkenlerini Ayarlayın**: .env dosyasını oluşturun ve aşağıdaki değişkenleri tanımlayın.

    GOOGLE_API_KEY: Google API anahtarınız.
HUGGINGFACE_TOKEN: Hugging Face token bilginiz.

## Kullanım
**POST /create-presentation** uç noktasını kullanarak PDF dosyasını işleyin ve sunum oluşturun.
API, PDF dosyasındaki metin içeriğini okuyacak, slayt başlıkları ve maddeleri oluşturacak, her slayt için uygun görsel terimlerini seçecek ve AI tabanlı görseller üretecektir.
Çıktı olarak bir PowerPoint sunum dosyası (pptx) oluşturulur ve belirtilen konuma kaydedilir.