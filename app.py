from flask import Flask, request
import requests
from pathlib import Path
import os
import json
from flask import Flask, request, render_template, jsonify, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World! Welcome to my Flask app."

@app.route('/chatwoot-webhook', methods=['POST'])
def handle_webhook():
    # Get the webhook data from Chatwoot
    data = request.json
 
    print(data)  # User's message from Chatwoot
    return data



if __name__ == '__main__':
    app.run(port=5000)
