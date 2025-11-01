
document.addEventListener('DOMContentLoaded', () => {
    const askButton = document.getElementById('ask-button');
    const questionInput = document.getElementById('question-input');
    const responseArea = document.getElementById('response-area');

    const askQuestion = async () => {
        const question = questionInput.value.trim();
        if (!question) return;

        // 1. Display user's question
        appendMessage(question, 'user');
        questionInput.value = '';

        // 2. Show a thinking message
        const thinkingMessage = appendMessage('Pensando...', 'bot');

        try {
            // 3. Send question to backend
            const response = await fetch('/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: question }),
            });

            if (!response.ok) {
                throw new Error(`Error del servidor: ${response.statusText}`);
            }

            const data = await response.json();
            
            // 4. Replace "thinking" with the actual answer
            thinkingMessage.innerHTML = `<p>${data.answer}</p>`;

        } catch (error) {
            console.error("Error al contactar al backend:", error);
            thinkingMessage.innerHTML = '<p>Lo siento, no pude conectarme con el servidor. Revisa la consola para más detalles.</p>';
            thinkingMessage.style.color = 'red';
        }
    };

    const appendMessage = (text, type) => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${type}-message`);
        messageDiv.innerHTML = `<p>${text}</p>`;
        responseArea.appendChild(messageDiv);
        responseArea.scrollTop = responseArea.scrollHeight; // Auto-scroll to bottom
        return messageDiv;
    };

    askButton.addEventListener('click', askQuestion);
    questionInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            askQuestion();
        }
    });
});
