from app import app
from flask import render_template, request, redirect, flash, url_for
from configuraciones import *
from forms import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/interact')
def interat():
    return render_template("interact.html")


@app.route('/feed')
def feed():
	form = FeedForm()
	#return redirect(url_for('index'))
	return render_template("feed.html", form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/petregister', methods=['GET', 'POST'])
def petregister():
    form = NewPet(request.form)
    if request.method == 'POST' and form.validate():
        pet = User(form.name.data, form.race.data,
                    form.size.data, form.colour.data)
        db_session.add(pet)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('petregister.html', form=form)


@app.route('/logs', methods=['GET', 'POST'])
def logs():
	historial =  request.form['historial']
        sql ="""select id,cantidad,tipo,fecha from historial"""
        print sql
        cur.execute(sql)
        logs  = cur.fetchall()

        return render_template("logs.html",logs = logs) 