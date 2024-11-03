# 🔑 Topic Test Generator

![quiz](https://github.com/Talha-Bicak/YolAI/blob/main/img/MiniTestQuestions.jpeg)

**The Topic Test Generator is an API service that automatically creates and evaluates multiple-choice questions from PDF files. It uses Google's Gemini AI model for content analysis and generates high-quality questions.**

![quiz](https://github.com/Talha-Bicak/YolAI/blob/main/img/MiniTestResult.jpeg)

## 🚀 Features

- **PDF Text Extraction**: Automatically extracts text content from PDF files.
- **AI-based smart question generation**: Creates questions with Gemini.
- **Multiple-choice question format support**: Convenient multiple-choice questions.
- **Automatic question evaluation system**: Question analysis with Gemini.
- **Detailed feedback and explanations**: Provides explanations for the correct answers.
- **Fast API design**: API connection for web interface.

## 🛠️ Installation

### Clone the repo:

git clone https://github.com/yourusername/pdf-quiz-generator.git
cd pdf-quiz-generator

### Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
```

#### or

```bash
.\venv\Scripts\activate  # For Windows
```

### Set your API key in the config file:

```bash
config.py
API_KEY = "your_gemini_api_key_here"
```

## 💡 For Use

### 1.Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000.


### 2. Sending a PDF and creating questions via Windows Powershell:

```bash
curl.exe -X POST "http://localhost:8000/upload-pdf/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@PDF_PATH"
```

### 3. Answering questions via Windows Powershell (example):

```bash
curl.exe -X POST "http://localhost:8000/submit-answers/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"answers":{"1":"A","2":"A","3":"A","4":"A","5":"A","6":"A","7":"A","8":"A","9":"A","10":"A"}}'
```

## 🔑 Required API Keys

The application requires the following API keys:

- **Google Gemini API**: For content generation

## 🔧 Technologies Used

- **FastAPI**: A fast and modern web framework.
- **Pydantic**: For data validation and modeling.
- **Google Generative AI (Gemini)**: Used to analyze responses to questions.
- **PyPDF**: PDF processing library for text extraction, analysis, and multi-page support.
- **Python 3.8+**
- **Uvicorn**

## 🔒 Security
CORS policies Exception handling Input validation API key verification

## 🤝 Contributing
Fork the repo Create a feature branch (git checkout -b feature/amazing-feature) Commit your changes (git commit -m 'feat: Add amazing feature') Push to the branch (git push origin feature/amazing-feature) Open a Pull Request

## 📜 License
This project is licensed under the MIT License. See the [LICENSE] file for details.

## 🙏 Acknowledgments
Google Gemini AI FastAPI team PyPDF developers

## 📞 Support & Contact
For support, please open an issue on the GitHub repository or contact the developers.
