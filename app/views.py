from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('layouts/base.html')

@app.route('/users/login')
def login():
    return render_template('users/login.html')
<<<<<<< HEAD

@app.route('/feed')
def feed():
    return render_template('layouts/feed.html')

@app.route('/about')
def about():
    return render_template('layouts/about.html')
=======
    
>>>>>>> 6a5602cd93be6960eb12b017ec805a71103f270c
