from flask import Flask, request, render_template
import subprocess

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/display', methods=['POST'])
def display():
	song_title = request.form['song_title']
	artist = request.form['artist']
	text = f"{song_title} - {artist}"
	
	# Call function to display text on the led 
	subprocess.run(["python3", "display_text.py", text])
	return 'Text sent to LED Matrix!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
