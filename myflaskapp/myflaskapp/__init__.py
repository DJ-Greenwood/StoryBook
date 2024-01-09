# app.py
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/story_elements')
def story_elements():
    with open('story_elements.json') as f:
        data = json.load(f)
    return render_template('story_elements.html', data=data)