import os
import google.generativeai as genai

# API Anahtarları
GOOGLE_API_KEY = 'AIzaSyCNgdn7KjbP0qG0JImezJl1D_cOApDnYQo'

genai.configure(api_key=GOOGLE_API_KEY)

# Imagen modelini oluşturun
imagen = genai.ImageGenerationModel("imagen-3.0-generate-001")

# Görsel oluşturma isteği
result = imagen.generate_images(
    prompt="Fuzzy bunnies in my kitchen",
    number_of_images=4,
    safety_filter_level="block_only_high",
    person_generation="allow_adult",
    aspect_ratio="3:4",
    negative_prompt="Outside",
)

# Oluşturulan görselleri gösterme
for image in result.images:
    image._pil_image.show()