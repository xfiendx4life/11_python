# project/tests/test_req.py

import unittest
import os

from project import app
from project.models import db, User, Note
from project.views import *

TEST_DB = 'test.db'

class RequestTests(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
			os.path.join(app.config['BASEDIR'], TEST_DB)
		app.secret_key = 'staytrue'
		cls.app = app.test_client()

	def setUp(self):
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_auth(self):
		u = User(username='Cyberslav', password='1234567', email='cyber@mail.ru')
		db.session.add(u)
		db.session.commit()
		response = self.app.post('/login', data=dict(username='Cyberslav', password='1234567'), follow_redirects=True)
		with self.app.session_transaction() as sess:
			self.assertEqual(sess['username'], 'Cyberslav')

	def test_logout(self):
		u = User(username='Cyberslav', password='1234567', email='cyber@mail.ru')
		db.session.add(u)
		db.session.commit()
		response = self.app.post('/login', data=dict(username='Cyberslav', password='1234567'), follow_redirects=True)
		resp = self.app.get('/logout', follow_redirects=True)
		with self.app.session_transaction() as sess:
			self.assertNotIn('Cyberslav', sess)

	def test_registration(self):
		response = self.app.post('/register', data=dict(username='Cyberslav', password='1234567', 
			email='123@mail.ru'), follow_redirects=True)
		u = User.query.filter_by(username='Cyberslav').first()
		self.assertEqual(u.password, '1234567')

	def test_failed_registration(self):
		u = User(username='Cyberslav', password='1234567', email='cyber@mail.ru')
		db.session.add(u)
		db.session.commit()
		response = self.app.post('/register', data=dict(username='Cyberslav', password='123', 
			email='123@mail.ru'), follow_redirects=True)
		self.assertIn(b'User exists. Check your login and email', response.data)

	def test_delete_note(self):
		u = User(username='Cyberslav', password='1234567', email='cyber@mail.ru')
		n = Note(head="Test note", body='test body for test note')
		u.notes.append(n)
		db.session.add(u)
		db.session.commit()
		response = self.app.get('/delete_note/1', follow_redirects=True)
		self.assertIs(Note.query.filter_by(head='Test note').first(), None)

	def test_delete_note_fault(self):
		u = User(username='Cyberslav', password='1234567', email='cyber@mail.ru')
		n = Note(head="Test note", body='test body for test note')
		u.notes.append(n)
		db.session.add(u)
		db.session.commit()
		response = self.app.get('/delete_note/2', follow_redirects=True)
		self.assertIn(b"Delete is broken", response.data)

if __name__ == "__main__":
    unittest.main()