from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

# Add the code for the search_playlist endpoint here
