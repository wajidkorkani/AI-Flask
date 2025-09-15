# Flask app with home page, SQLite DB, and message table

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Message model
class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(255), nullable=False)

# Create tables
with app.app_context():
	db.create_all()

@app.route('/')
def home():
	messages = Message.query.all()
	return render_template('index.html', messages=messages)

if __name__ == '__main__':
	app.run(debug=True)
