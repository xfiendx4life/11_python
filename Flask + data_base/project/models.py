from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)
	
    def __repr__(self):
        return self.username

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	head = db.Column(db.String(80), unique=True, nullable=False)
	body = db.Column(db.Text, unique=True, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return self.head
