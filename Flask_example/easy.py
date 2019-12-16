from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route('/index')
def hello_world():
	return '''
		<a href="/index/pokupki"> Покупки </a>
		<br>
		<a href="/index/rabota"> Работа </a>
	'''

@app.route('/index/<name>')
def chek(name):
	return 'Хэллоу %s' % name


if __name__ == '__main__':
	app.run(debug=True)