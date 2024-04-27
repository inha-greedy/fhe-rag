// Add file drag and drop functionality
const uploadAreas = document.querySelectorAll('.upload-area');
uploadAreas.forEach(area => {
    area.addEventListener('dragover', (e) => {
        e.preventDefault();
        area.classList.add('dragover');
    });

    area.addEventListener('dragleave', () => {
        area.classList.remove('dragover');
    });

    area.addEventListener('drop', (e) => {
        e.preventDefault();
        area.classList.remove('dragover');
        const files = e.dataTransfer.files;
        console.log(files);
        // Add your file handling logic here
    });
});

// Add chat input functionality
const chatInput = document.querySelector('.chat-input input');
const chatMessages = document.querySelector('.chat-messages');

chatInput.addEventListener('keydown', (e) => {
    if (e.keyCode === 13) { // Enter key
        const message = chatInput.value.trim();
        if (message) {
            addMessage('client', message);
            chatInput.value = '';
            // Add your chatbot logic here
            addMessage('bot', 'This is a sample bot response.');
        }
    }
});

function addMessage(type, text) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', type);
    messageDiv.textContent = `${type}: ${text}`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}