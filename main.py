import os
from flask import Flask, request, redirect
import requests

BOT_TOKEN = os.getenv('BOT_TOKEN', '8067010246:AAGDH1QipjvFW0cY2t2a-iy_bkPFVnliXxY')

app = Flask(__name__)

@app.route('/<file_id>')
def get_file(file_id):
    # Telegram file download link format
    download_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_id}"
    return redirect(download_url)

@app.route('/')
def index():
    return "Telegram File Link Bot is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
