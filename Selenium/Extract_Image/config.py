class Config:
    """Uygulama yapılandırma sınıfı"""

    # Varsayılan screenshot dizini
    DEFAULT_SCREENSHOT_PATH = "../../screenshots"

    # Varsayılan görüntü sayısı
    DEFAULT_NUM_IMAGES = 5

    # Bekleme süreleri (saniye)
    WAIT_TIMES = {
        "page_load": 2,
        "search": 3,
        "scroll": 1,
        "screenshot": 1
    }

    # Selenium ayarları
    SELENIUM_TIMEOUT = 10

    # CSS Selectors
    SELECTORS = {
        "search_box": "q",  # name attribute
        "thumbnails": "div.H8Rx8c"  # class
    }