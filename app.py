import logging
from flask import Flask, request, render_template, jsonify
import subprocess

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display', methods=['POST'])
def display():
    song_title = request.form['song_title']
    artist = request.form['artist']
    text = f"{song_title} - {artist}"
    try:
        result = subprocess.run(
            ["python3", "display_text.py", text], capture_output=True, text=True, check=True
        )
        logging.info(f"Displayed text: {text}")
        return jsonify({'message': 'Text sent to LED Matrix!', 'status': 'success'})
    except subprocess.CalledProcessError as e:
        error_message = e.stdout + e.stderr
        logging.error(f"Error displaying text: {text} - {error_message}")
        return jsonify({'message': 'Error sending text to LED Matrix: ' + error_message, 'status': 'error'}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'message': 'An unexpected error occurred.', 'status': 'error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
