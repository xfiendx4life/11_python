from flask import Flask, request, escape, redirect, url_for 
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
	return  render('more.html', name=name) 

'''@app.route('/request-test', methods=['GET', 'POST'])
def request_test():
	if request.method == 'POST':
		name = request.form['data']
		return redirect(url_for('note', name=name))
	else:
		return render('requests_ex.html')'''

@app.route('/request-test')
def request_test():
	if 'data' in request.args.keys():
		name = request.args.get('data')
		return redirect(url_for('note', name=name))
	return render('requests_ex.html')
		

if __name__ == '__main__':
    app.run(debug=True)