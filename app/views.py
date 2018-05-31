from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('layouts/base.html')

@app.route('/users/login')
def login():
    return render_template('users/login.html')
    