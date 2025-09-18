from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

app = Flask(__name__)

# Configure with your API key
genai.configure(api_key="AIzaSyDwZ1UUPkakY04l-a4OXXUETMLU19rIsXo")

# Choose a model (gemini-1.5-flash is fast, gemini-1.5-pro is smarter)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = []

@app.route('/')
def home():
	return render_template('index.html', messages=chat)


@app.route('/add', methods=['POST'])
def add_message():
	text = request.form['text']
	response = model.generate_content(text)
	response = response.text.replace("*", "")
	response = response.replace("\"", "")
	chat.append({
		"question":text,
		"answer":response
		})
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)
