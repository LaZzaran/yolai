#### Yetkiliye Not: Bu bölüm bitirildikten sonra, ücretli kredilendirme bulunduğu tespit edilmiş, adil bir yarışma olması için kullanılmamıştır.
<p>
Bu repo alıntıdır.
</p>

# Heygen Interactive Avatar Integration for Autonomous PDF Presentation

This project uses the Heygen API to create a dynamic, interactive presentation experience. Given any PDF, the system autonomously generates a presentation, and an interactive avatar (powered by Heygen) narrates the content. The avatar also responds to questions, using the PDF as contextual material to provide answers based on the curriculum content.

For competition purposes, SadTalker was used as a substitute for Heygen due to Heygen's paid API model. Below is a detailed guide on setting up the Heygen integration.

---

## Project Features

1. **Autonomous PDF-to-Presentation Conversion:** Takes any PDF and automatically generates a structured presentation.
2. **Interactive Avatar Narration:** Uses Heygen’s API to provide a life-like avatar that narrates the presentation content in real time.
3. **Student Interaction:** Allows the avatar to respond to questions, utilizing the PDF context to provide relevant answers.

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd <your-repo-directory>
```

### 2. Install Dependencies

Ensure Node.js and npm are installed on your system.

```bash
npm install
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your Heygen API key to enable access to the Interactive Avatar features.

```plaintext
HEYGEN_API_KEY=your_heygen_api_key
```

> **Note:** If you also plan to connect to GEMINI for LLM functionality, add your GEMINI API key here.

```plaintext
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Run the Application

Start the development server.

```bash
npm run dev
```

---

## Using the Interactive Avatar

### Starting a Session

- Click on the “Start” button on the presentation interface to activate the Heygen avatar.
- Enter text in the input box, then hit Enter. The avatar will read the entered text.
- Close the session to start over or switch avatars.

### Customizing the Avatar

You can select different avatars and voices within the Heygen system. Obtain avatar IDs from [app.heygen.com/interactive-avatar](https://app.heygen.com/interactive-avatar) and set these IDs in your configuration.

---

## Connecting to GEMINI (Optional)

To enhance interactivity, connect the avatar with an LLM like ChatGPT:

1. Place your GEMINI API key in the `.env` file.
2. The system will then use the GEMINI API to provide intelligent responses based on user queries related to the PDF content.

---

## Avatar IDs and Customization

Heygen offers several public avatars for Interactive Avatar functionality. To use private avatars, you’ll need to upgrade them on the Heygen platform.

---

## Enterprise and Trial Tokens

- **Trial Token**: Limited to 3 free concurrent sessions.
- **Enterprise API Token**: Supports increased session limits for high-usage environments.

For more on Heygen’s Interactive Avatar API and enterprise usage, visit [Interactive Avatar 101](https://help.heygen.com/en/articles/9182113-interactive-avatar-101-your-ultimate-guide).

---

Feel free to explore and extend this integration for customized interactive experiences!
