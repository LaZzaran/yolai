import google.generativeai as genai

class Config:
    GOOGLE_API_KEY = 'AIzaSyAT8sDfuOOwSbl_3_8KZoWdZQgyKI-XWJA'
    genai.configure(api_key=GOOGLE_API_KEY)