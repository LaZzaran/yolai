import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_GOOGLE_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "your_hugging_face_token")
OUTPUT_IMAGE_DIR = "/stabilityai/downloaded_images"  # Görsellerin kaydedileceği dizin
OUTPUT_PRESENTATION_DIR = "/stabilityai/presentations"  # Sunumların kaydedileceği dizin
MODEL_NAME = "gemini-1.5-pro"
PIPELINE_MODEL_PATH = "stabilityai/stable-diffusion-3.5-large"