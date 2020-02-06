from flask import Flask, redirect, url_for, make_response, session, request
import os
from .base_processing import *
import jinja2
from . import app

#template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.PackageLoader('project', 'templates'), autoescape = True)


def render(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

@app.route('/')
def index():
	if 'username' in session:
		notes = get_note_list(session['username'])
		return render('notes.html', notes=notes, name=session['username'])
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username and password and authenticate(username, password):
			session['username'] = username
			return redirect(url_for('index'))
	return render('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		if username and password and email and register(username, password, email):
			session['username'] = username
			return redirect(url_for('index'))
	return render("register.html")

@app.route('/note/<name>')
def note(name):
	if 'username' in session:
		note = get_note(name, session['username'])
		return render('note.html', head=note.head, body=note.body)
	return redirect(url_for('login'))

@app.route('/add_note', methods=['GET', 'POST'])
def add_note_view(note=''):
	if 'username' in session:
		if request.method == 'POST':
			if request.form['head'] and request.form['body'] and add_note(request.form['head'], request.form['body'], session['username']):
				return redirect(url_for('index'))
		return render('edit_note.html', note=note)
	return redirect(url_for('index'))

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))