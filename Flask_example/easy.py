from flask import Flask
from flask import escape
import jinja2
import os

app = Flask(__name__)

template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


def render(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

@app.route('/index')
def hello_world():
	l = ['Камень', 'Подорожник', 'Лопух']
	return render('1.html', name='Пацан', items=l)

@app.route('/index/<name>')
def chek(name):
	return render('2.html')


if __name__ == '__main__':
	app.run(debug=True)