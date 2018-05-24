from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/test')
def test():
    return render_template("test.html")
    