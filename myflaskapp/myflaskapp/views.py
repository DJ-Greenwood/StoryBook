# myflaskapp/myflaskapp/views.py
# myflaskapp/myflaskapp/views.py
from myflaskapp import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/story_elements")
def story_elements():
    return render_template('story_elements.html')