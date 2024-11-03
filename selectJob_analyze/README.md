# 💻 Career Test API

![meslek](https://github.com/Talha-Bicak/YolAI/blob/main/img/JobTestOuestions.jpeg)

This project is a career counseling API developed using FastAPI and Google's Gemini AI model. It analyzes users' interests, abilities, and preferences by asking a series of questions and provides personalized career suggestions.

![meslek](https://github.com/Talha-Bicak/YolAI/blob/main/img/JobTestResult.jpeg)

## 🌟 Features

- **Interactive Q&A system**
- **Career analysis powered by Google Gemini AI**
- **Fast API endpoints**
- **Session management**
- **CORS support**
- **UTF-8 character support**
- **Error handling**

## 📄 File Descriptions
- **models.py**: Contains data models like Answer and SessionState. Pydantic is used to ensure the validity of user responses.
- **questions.py**: File where questions are stored in UTF-8 format.
- **gemini_service.py**: Module that handles communication with Google Generative AI (Gemini) API. Configures API key, creates model, and performs response analysis.
- **session_manager.py**: Manages user sessions and responses. Tracks user progress and handles session reset.
- **main.py**: Main file of the FastAPI application. All endpoints are defined here and the application runs here.

## 🚀 Installation:

### 1. Install required packages:

```bash
pip install -r requirements.txt
```

## 🔑 Required API Keys

The application requires the following API keys:

- **Google Gemini API**: For content generation

## 📝 API Endpoints:

**GET /**
Homepage
List of available API endpoints

**GET /current-question**
Retrieves current question
Total question count and progress information

**POST /submit-answer**
Submits answer to current question
Moves to next question
Initiates AI analysis when all questions are completed

**GET /progress**
Shows current progress status
Completed question count and percentage information

**POST /reset**
Resets session
Starts a new test

## 💡 For Use

### 1. Running the Application

Start the FastAPI server:
```bash
uvicorn src.main:app --reload
```

API will be available at `http://localhost:8000`.

### Requesting questions via Windows Powershell:

```bash
Invoke-RestMethod -Uri "http://localhost:8000/current-question" -Method Get
```

### Submitting answers via Windows Powershell:

```bash
Invoke-RestMethod -Uri "http://localhost:8000/submit-answer" -Method Post -Body ([System.Text.Encoding]::UTF8.GetBytes((@{answer="YOUR_ANSWER"} | ConvertTo-Json))) -ContentType "application/json; charset=utf-8"
```

## 🛠️ Technologies

- **FastAPI**: A fast and modern web framework.
- **Pydantic**: Used for data validation and modeling.
- **Google Generative AI (Gemini)**: Used to analyze responses to questions.
- **CORS Middleware**: For handling cross-origin requests.
- **Python 3.8+**
- **Uvicorn**

## 🔒 Security

- **CORS policies**
- **Exception handling**
- **Input validation**
- **API key validation**

## 🤝 Contributing

- **Fork this project**
- **Create feature branch**: (git checkout -b feature/AmazingFeature)
- **Commit your changes**: (git commit -m 'Add some AmazingFeature')
- **Push to branch**: (git push origin feature/AmazingFeature)
- **Create Pull Request**

## 📄 License

This project is licensed under MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support and Contact

For support, please open an issue in the GitHub repository or contact the developers.
