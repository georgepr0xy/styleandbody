from flask import Flask, render_template, redirect, url_for
from config import CHAT_CONFIG

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat/<chat_type>')
def chat(chat_type):
    chat_data = CHAT_CONFIG.get(chat_type, {})
    if not chat_data:
        return "Chat type not found", 404
    return render_template('chat.html', title=chat_data['title'], description=chat_data['description'])

if __name__ == '__main__':
    app.run(debug=True)