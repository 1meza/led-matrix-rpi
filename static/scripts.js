document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('display-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/display', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const messageDiv = document.getElementById('message');
            if (data.status === 'success') {
                messageDiv.textContent = data.message;
                messageDiv.className = 'text-success';
            } else {
                messageDiv.textContent = data.message;
                messageDiv.className = 'text-danger';
            }
            form.reset();
        })
        .catch(error => {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = 'An error occurred while sending the text to the LED Matrix.';
            messageDiv.className = 'text-danger';
            console.error('Error:', error);
        });
    });
});
