from db import *
from funcs import *
import unittest
from sqlalchemy.orm import sessionmaker
import time

class TestDb(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		engine = create_engine('sqlite:///bf.db')
		TestDb.Session = sessionmaker()
		TestDb.Session.configure(bind=engine)

	def setUp(self):
		self.session = TestDb.Session()
		p = Person('pacan', 'qwerty', 'Chetkiy')
		p1 = Person('chika', '1234', 'Beautiful')
		p2 = Person('doter', '12345', 'Very communicative')
		self.session.add_all([p, p1, p2])
		self.session.commit()

	def tearDown(self):
		self.session.query(Person).delete()
		self.session.commit()
		self.session.close()

	def test_authenticate_true(self):
		self.assertTrue(authenticate(self.session, 'chika', '1234'))

	def test_authenticate_session(self):
		authenticate(self.session, 'chika', '1234')
		p = self.session.query(Person).filter(Person.login == 'chika').first()
		s = self.session.query(UserSession).filter(UserSession.user_id == p.id).first()
		self.assertTrue(s)

	def testLogout(self):
		authenticate(self.session, 'pacan', 'qwerty')
		time.sleep(2)
		logout(self.session, 'pacan')
		#p = self.session.query(Person).filter(Person.login == 'pacan').first()
		s = self.session.query(UserSession).filter(UserSession.user_id == 1).first()
		self.assertTrue(s.start_time < s.finish_time)

	def test_authenticate_wrong_password(self):
		self.assertFalse(authenticate(self.session, 'chika', '12345'))

	def test_authenticate_no_data_in_db(self):
		self.assertFalse(authenticate(self.session, 'chikulya', '1234'))

	def test_register(self):
		register(self.session, 'poc', '234', 'Chetchaishiy')
		p = self.session.query(Person).filter(Person.login == 'poc').first()
		self.assertEqual(p.login, 'poc')

	def test_register_used_login(self):
		self.assertFalse(register(self.session, 'pacan', 'qwerty', 'Chetkiy'))

	


if __name__ == "__main__":
	unittest.main(failfast=True)
