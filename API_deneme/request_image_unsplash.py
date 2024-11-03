import requests

response = requests.get('https://api.unsplash.com/search/photos', params={
    'query': ' visceral organ',
    'client_id': 'Your_clientid'
})

data = response.json()
print(data)
image_url = data['results'][0]['urls']['small_s3']

# Resim URL'sinden içeriği al
image_response = requests.get(image_url)

# Resmi mevcut dizine "rose_image.jpg" olarak kaydet
if image_response.status_code == 200:
    with open("rose_image.jpg", "wb") as file:
        file.write(image_response.content)
    print("Resim başarıyla indirildi ve kaydedildi.")
else:
    print("Resim indirilemedi.")
