from flask import Flask, session, request, escape, redirect, url_for, make_response
import jinja2
import os


app = Flask(__name__)
app.secret_key = 'ea5f3c96bf0aad59c65019c5ea11689f5d9f5f8f13ec426aa4cf7c6e5835a8b4'

#-------------------------------Подготовка шаблонов---------------------#
template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


def render(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

#-------------------------------Обработка страницы веб-приложения---------------------#
@app.route('/index')
def hello_world():
	items = ['ЖАБА!', 'Динозавр', 'Семён']
	return render('index.html', name='Человек', items=items)

@app.route('/note/<name>')
def note(name):
	return  render('more.html', name=name) 

#-------------------------------Обработка POST-запроса---------------------#
@app.route('/request-test', methods=['GET', 'POST'])
def request_test():
	if request.method == 'POST':
		name = request.form['login']
		# заполнить базу данных
		return redirect(url_for('note', name=name))
	else:
		return render('requests_ex.html')

#-------------------------------Обработка GET-запроса---------------------#
@app.route('/request-test-get')
def request_test_get():
	if 'data' in request.args.keys():
		name = request.args.get('data')
		return redirect(url_for('note', name=name))
	return render('requests_ex_get.html')

#-------------------------------Запись данных в объект session---------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		name = request.form['login']
		password = request.form['password']
		session['username'] = name
		return redirect(url_for('success'))
	return render('requests_ex.html')

#-------------------------------Чтение данных из объекта session---------------------#
@app.route('/success')
def success():
	if 'username' in session:
		return 'WELCOME ABOARD, %s' % escape(session['username'])
	return '<h1> =( </h1>'

#-------------------------------Удаление данных из объекта session---------------------#
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    if 'username' in session:
    	session.pop('username')
    return redirect(url_for('login'))

#-------------------------------Установка cookie--------------------------------------#
@app.route('/set_cookie')
def set_c():
	resp = make_response(render('1.html'))
	resp.set_cookie('login', 'Cyberslav', max_age=282)
	return resp

#-------------------------------Удаление cookie--------------------------------------#
@app.route('/check_cookie')
def check():
	login = request.cookies.get('login')
	return 'Hello: ' + login


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2')