from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ola')
def ola():
    return '<h1>Olá Mundo Flask!</h1>'
