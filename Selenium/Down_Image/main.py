from image_downloader import ImageDownloader

if __name__ == "__main__":
    keyword = "Kedi"  # Aranacak kelime
    download_path = "downloaded_images"  # İndirme klasörü
    num_images = 5

    downloader = ImageDownloader(keyword, download_path, num_images)
    total_downloaded = downloader.download_images()
    print(f"Toplam {total_downloaded} resim başarıyla indirildi.")
