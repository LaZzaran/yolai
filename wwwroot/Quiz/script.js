async function uploadPDF() {
    try {
        const response = await fetch('/Exam/UploadPDF', {
            method: 'POST'
        });

        const result = await response.json();
        if (result.success) {
            displayQuestions(JSON.parse(result.questions).sorular);
        } else {
            alert('Hata: ' + result.error);
        }
    } catch (error) {
        console.error('Hata:', error);
        alert('Bir hata oluştu: ' + error.message);
    }
}

function displayQuestions(questions) {
    const form = document.getElementById('answer-form');
    form.innerHTML = '';
    questions.forEach((question, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');
        questionDiv.innerHTML = `<p>${index + 1}. ${question.question}</p>`;

        question.options.forEach((option, optIndex) => {
            const optionDiv = document.createElement('div');
            optionDiv.classList.add('option');

            const radioInput = document.createElement('input');
            radioInput.type = 'radio';
            radioInput.name = `question_${index + 1}`;
            radioInput.value = String.fromCharCode(65 + optIndex);
            radioInput.required = true;

            const label = document.createElement('label');
            label.innerText = `${String.fromCharCode(65 + optIndex)}: ${option}`;

            optionDiv.appendChild(radioInput);
            optionDiv.appendChild(label);
            questionDiv.appendChild(optionDiv);
        });

        form.appendChild(questionDiv);
    });

    document.getElementById('questions-section').style.display = 'block';
}

async function submitAnswers()
{
    const formData = new FormData(document.getElementById('answer-form'));
    const answers = {};
    formData.forEach((value, key) => {
        const questionIndex = parseInt(key.split('_')[1]);
        answers[questionIndex] = value;
    });

    try {
        const response = await fetch('http://localhost:8000/submit-answers/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cevaplar: answers })
        });

        const result = await response.json();
        if (response.ok) {
            localStorage.setItem('examResult', JSON.stringify(result));
            window.location.href = '/Exam/Results';
        } else {
            alert('Hata: ' + result.detail);
        }
    } catch (error) {
        console.error('Hata:', error);
        alert('Bir hata oluştu: ' + error.message);
    }
}
