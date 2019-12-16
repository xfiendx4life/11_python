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
	items = ['Лягушка', 'Динозавр', 'Семён']
	return render('index.html', name='Человек', items=items)

@app.route('/note/<name>')
def note(name):
	return  render('more.html', name=escape(name)) 

if __name__ == '__main__':
    app.run(debug=True)