<<<<<<< HEAD
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
	sql ="""
	select id,nombre from categorias order by nombre
	"""
	print(sql) 
	cur.execute(sql)
	categorias  = cur.fetchall()
	sql ="""
	select id,titulo,resumen from posts
	"""
	print(sql)
	cur.execute(sql)
	posts  = cur.fetchall()
	return render_template("index.html",categorias=categorias,posts=posts)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
	if request.method == 'POST':
		comentario =  request.form['comentarios']
		print(comentario)
		sql = """ insert into comentarios  
		(post_id,usuario_id,creado,comentario) 
		values (%s,1,now(),'%s' ) """%(post_id,comentario)
		cur.execute(sql)
		conn.commit()

	sql ="""
	select id,titulo,texto from posts where id = %s
	"""%post_id
	print(sql)
	cur.execute(sql)
	post  = cur.fetchone()

	sql ="""
	select id,nombre from categorias,categorias_posts 
	where categorias_posts.categoria_id = categorias.id 
	and post_id = %s 
	"""%(post_id)
	print(sql)
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select comentarios.id,nombre,apellido,comentario
	
	from usuarios,comentarios 
	where comentarios.usuario_id = usuarios.id 
	and post_id = %s order by id desc
	"""%(post_id)
	print(sql)
	cur.execute(sql)
	comentarios  = cur.fetchall()
	return render_template("post.html",post= post,categorias=categorias,comentarios= comentarios) 


@app.route('/comentario/<id>', methods=['GET', 'POST'])
def comentario(id):
	if request.method == 'POST':
		comentario =  request.form['comentarios']
		print(comentario)
		sql = """ update comentarios  set comentario = '%s'
		where id = %s """%(comentario,id)
		cur.execute(sql)
		conn.commit()


	sql ="""
	select comentarios.id,nombre,apellido,comentario
	
	from usuarios,comentarios 
	where comentarios.usuario_id = usuarios.id 
	and comentarios.id = %s order by id desc
	"""%(id)
	print(sql)
	cur.execute(sql)
	comentario  = cur.fetchone()
	return render_template("comentario.html",comentario= comentario) 


@app.route('/borrar/<id>', methods=['GET', 'POST'])
def borrar(id):


	sql ="""
		delete from comentarios where id = %s
	"""%(id)
	print(sql)
	cur.execute(sql)
	conn.commit()
	return  redirect(request.referrer)

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
=======
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
>>>>>>> 2a7ff4b1c703d4905ad846630aeab3621467d0fa
