from flask import Flask, redirect, url_for, make_response, session

import os
from .base_processing import *
import jinja2

from . import app



template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


def render(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

@app.route('/')
def index():
	if 'username' in session:
		notes = get_note_list(session['username'])
		if notes:
			return render('notes.html', notes=notes, name=session['username'])
	return redirect(url_for('login'))

@app.route('/login')
def login():
	session['username']='Cybersslav'
	return 'login'

@app.route('/note/<name>')
def note(name):
	if 'username' in session:
		note = get_note(name, session['username'])
		return render('note.html', head=note.head, body=note.body)
	return redirect(url_for('login'))