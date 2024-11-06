import json
import google.generativeai as genai

class SlideContentGenerator:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 8192
            }
        )

    def create_structured_prompt(self, text):
        return f"""
        Lütfen aşağıdaki metinden profesyonel bir sunum oluştur...
        Metin: {text}
        ...
        """

    def get_presentation_content(self, text):
        prompt = self.create_structured_prompt(text)
        response = self.model.generate_content(prompt)

        try:
            content = json.loads(response.text)
            for slide in content['slides']:
                if 'image_keyword' in slide:
                    search_term = slide['image_keyword']['search_term'] + " high quality educational"
                    slide['image_keyword']['search_term'] = search_term
            return content
        except json.JSONDecodeError:
            cleaned_response = response.text.strip()
            cleaned_response = cleaned_response[cleaned_response.find('{'):cleaned_response.rfind('}') + 1]
            return json.loads(cleaned_response)
