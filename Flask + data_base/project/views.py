from flask import Flask, redirect, url_for, make_response, session, request, render_template
import os
from .base_processing import *
import jinja2
from . import app

#template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.PackageLoader('project', 'templates'), autoescape = True)
jinja_env.globals['STATIC_PREFIX'] = '/'

def render(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

@app.route('/')
def index():
	if 'username' in session:
		notes = get_note_list(session['username'])
		return render_template('notes.html', notes=notes, name=session['username'])
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username and password and authenticate(username, password):
			session['username'] = username
			return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		if username and password and email and register(username, password, email):
			session['username'] = username
			return redirect(url_for('index'))
	return render_template("register.html")

@app.route('/note/<name>')
def note(name):
	if 'username' in session:
		note = get_note(name, session['username'])
		return render_template('note.html', head=note.head, body=note.body)
	return redirect(url_for('login'))

@app.route('/add_note', methods=['GET', 'POST'])
def add_note_view(note=''):
	if 'username' in session:
		if request.method == 'POST':
			if request.form['head'] and request.form['body'] and add_note(request.form['head'], request.form['body'], session['username']):
				return redirect(url_for('index'))
		return render_template('edit_note.html', note=note)
	return redirect(url_for('index'))

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	# Если исключение было вызвано ошибкой взаимодействия с базой данных, 
	# нам необходимо откатить текущую сессию.
    db.session.rollback()
    return render_template('500.html'), 500