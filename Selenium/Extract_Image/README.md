# 🔍 Görsel Tutucu Botu


Bu proje, Selenium WebDriver kullanarak Google Görseller'den resim bölümlerini yakalamayı otomatikleştiren Nesne Yönelimli bir Python uygulamasıdır. Modüler, bakımı kolay ve kullanımı basit olacak şekilde tasarlanmıştır.

## 🌟 Özellikler

- **Otomatik görsel div yakalama**
- **OOP mimarisi**
- **Yapılandırılabilir ayarlar**
- **Hata yönetimi**
- **Chrome WebDriver desteği**
- **Ekran görüntüsü yönetimi**
- **İlerleme takibi**

## 🏗️ Proje Yapısı

```bash
GörselTutucu/
│
├── src/
│   ├── __init__.py
│   ├── google_image_scraper.py    # Ana scraper sınıfı
│   ├── config.py                  # Yapılandırma ayarları
│   └── requirements.txt           # Gerekli paketler
│
└── main.py                        # Uygulama giriş noktası
```

## 📄 Dosya Açıklamaları

- **google_image_scraper.py**: Tüm scraping işlemlerini yöneten ana GoogleImageScraper sınıfını içerir.
- **config.py**: Yapılandırma ayarlarını ve sabitleri saklar.
- **main.py**: Kullanım örnekleriyle birlikte uygulamanın giriş noktası.

## 🚀 Kurulum
- **1. Repository'yi klonlayın**:
bashCopygit clone https://github.com/kullaniciadi/google-image-scraper.git
cd google-image-scraper
- **2. Gerekli paketleri yükleyin**:
bashCopypip install -r requirements.txt
- **3. Chrome WebDriver'ı yükleyin**:
Chrome tarayıcısının yüklü olduğundan ve Chrome sürümünüze uygun ChromeDriver'ın bulunduğundan emin olun.

## 🔧 Gereksinimler

- **Python 3.8+**
- **Selenium WebDriver**
- **Chrome Tarayıcı**
- **ChromeDriver**
- **İşletim Sistemi: Windows/Linux/MacOS**

## 📝 Kullanım

```bash
python main.py
```

## 💡 Temel Özellikler
- **1. Otomatik Ekran Görüntüsü Yakalama**

Otomatik olarak her resme kaydırma
Yüksek kaliteli ekran görüntüleri
Dosya adlandırma ve depolama yönetimi

- **2. Hata Yönetimi**

Ağ sorunları için güçlü hata yönetimi
Sorunsuz hata kurtarma
Detaylı hata günlüğü

- **3. Kaynak Yönetimi**

Tarayıcı örneklerinin otomatik temizlenmesi
Verimli bellek kullanımı
Düzgün oturum yönetimi

## 🛠️ Teknolojiler

- **Python**: Ana programlama dili
- **Selenium**: Web otomasyonu
- **Chrome WebDriver**: Tarayıcı otomasyonu
- **Type Hints**: Kod dokümantasyonu
- **OOP Prensipleri**: Kod organizasyonu

## 🔒 Güvenlik Özellikleri

- **Güvenli dosya işleme**
- **Kaynak temizleme**
- **Hata yönetimi**
- **Girdi doğrulama**

## 🤝 Katkıda Bulunma

- **Repository'yi fork edin**
- **Feature branch'inizi oluşturun**: git checkout -b feature/YeniOzellik
- **Değişikliklerinizi commit edin**: git commit -m 'YeniOzellik eklendi'
- **Branch'e push edin**: git push origin feature/YeniOzellik
- **Pull Request açın**

## 📋 Yapılacaklar

 Diğer tarayıcılar için destek ekleme
 Paralel işleme desteği
 Görüntü format seçimi
 Proxy desteği
 Gelişmiş filtreleme seçenekleri

## 📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## 🙏 Teşekkürler

Web otomasyon aracı için Selenium ekibine
Bu projenin geliştirilmesine yardımcı olan tüm katkıda bulunanlara

## 📞 Destek
Destek için lütfen GitHub repository'sinde bir issue açın veya geliştiricilerle iletişime geçin.