# project/test_req.py

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
		pass



if __name__ == "__main__":
    unittest.main()