# myflaskapp/myflaskapp/views.py
from myflaskapp import app
@app.route("/")
def index():
    return "Hello, World!"