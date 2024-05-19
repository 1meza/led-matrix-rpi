document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('display-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/display', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('message').textContent = 'Text sent to LED Matrix!';
            form.reset();
        })
        .catch(error => {
            document.getElementById('message').textContent = 'Error sending text to LED Matrix.';
            console.error('Error:', error);
        });
    });
});
