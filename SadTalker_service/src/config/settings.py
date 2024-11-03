import os

class Settings:
    XI_API_KEY = os.getenv('ELEVEN_LABS_API_KEY', 'YOUR_APİ_KEY')
    VOICE_ID = os.getenv('ELEVEN_LABS_VOICE_ID', 'YOUR_APİ_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'YOUR_APİ_KEY')
    CHUNK_SIZE = 1024
    SADTALKER_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "SadTalker")