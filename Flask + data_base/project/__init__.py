from flask import Flask
  
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
 
from . import views