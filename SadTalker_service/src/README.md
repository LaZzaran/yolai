# 🚀 AI-Powered Presentation Generator

IMAGE!!!!

This project is an AI-powered presentation creation system that automatically generates professional PowerPoint presentations from PDF documents. It includes features such as automatic image selection, text-to-speech conversion, and talking head video generation.

## 🌟 Features

- **PDF Text Extraction**: Automatic text content extraction from PDF files
- **AI-Powered Content Generation**: Using Google's Gemini 1.5 Pro model to structure presentation content
- **Automatic Image Selection**: Finding relevant images for slides through Google Images
- **Text-to-Speech**: Creating natural voice narration using ElevenLabs API
- **Avatar Generation**: Creating realistic talking head videos using SadTalker
- **Professional PowerPoint Generation**: Creating well-structured PowerPoint presentations with proper formatting

## 🛠️ Core Components

### 1. AI Service (src/services/ai_service)
- Uses Google's Gemini 1.5 Pro model for content generation
- Structures presentation content with appropriate slide organization
- Generates relevant image search terms

### 2. Presentation Service (src/services/presentation_service)
- Creates professional PowerPoint presentations
- Manages slide layouts and formatting
- Integrates images and videos

### 3. Image Service (src/services/image_service)
- Searches and downloads relevant images
- Manages image processing and format conversion
- Maintains appropriate aspect ratios

### 4. Audio Service (src/services/audio_service)
- Creates natural speech from text
- Manages audio file handling
- Supports multiple languages

### 5. SadTalker Service (src/services/sadtalker_service)
- Generates talking head videos
- Integrates with presentation slides
- Manages video processing and optimization

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-presentation-generator.git
cd ai-presentation-generator
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set environment variables:

```bash
export ELEVEN_LABS_API_KEY='your_api_key'
export ELEVEN_LABS_VOICE_ID='voice_id'
export GOOGLE_API_KEY='your_google_api_key'
```

## Running the Application

### Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000.

## 📝 API Usage

### Creating a Presentation (via Windows Powershell)

```bash
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/create-presentation" -ContentType "application/json" -Body "{`"pdf_path`": `"YOUR_PDF_PATH`"}"
```

## 🔑 Required API Keys

The application requires the following API keys:

- **Google Gemini API**: For content generation
- **ElevenLabs API**: For text-to-speech conversion
- **Google Custom Search API**: For image search functionality

## 📚 Dependencies

- **`fastapi`**: Web framework
- **`pydantic`**: Data validation
- **`google-generativeai`**: Gemini AI integration
- **`python-pptx`**: PowerPoint creation
- **`PyPDF2`**: PDF processing
- **`selenium`**: Web scraping
- **`Pillow`**: Image processing
- **`requests`**: HTTP client
- **`google-cloud-texttospeech`**: Text-to-speech conversion

## 🤝 Contributing

We welcome your contributions! Please don't hesitate to send a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **SadTalker for avatar**
- **ElevenLabs for text-to-speech capabilities**
- **Google for the Gemini AI model**

## 📞 Support and Contact

For contact, please open an issue in the GitHub repository or get in touch with the developers.