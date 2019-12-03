import unittest
from driver import *
import sqlite3

class Test_db(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("my_beautiful_db.db")


	def tearDown(self):
		cursor = self.conn.cursor()
		cursor.execute('DELETE FROM Student')
		cursor.execute('DELETE FROM Marks')
		self.conn.commit()
		self.conn.close()


	def testAdd(self):
		self.assertTrue(add(self.conn, 'Cyberslav', 'Petrov'))

	def testAddWithQuery(self):
		cursor = self.conn.cursor()
		add(self.conn, 'Cyberslav', 'Petrov')
		cursor.execute("SELECT name From Student WHERE name = 'Cyberslav' and lastname ='Petrov' ")
		self.assertEqual(cursor.fetchone()[0], 'Cyberslav')

	def testAddFalse(self):
		cursor = self.conn.cursor()
		add(self.conn, 'Cyberslav', 'Petrov')
		self.assertFalse(add(self.conn, 'Cyberslav', 'Petrov'))


	def testAddMark(self):
		add(self.conn, 'Cyberslav', 'Petrov')
		self.assertTrue(addMark(self.conn, 'Cyberslav', 'Petrov', math=5, physics=3, russian=2))

	def testAddMarkWithQuery(self):
		add(self.conn, 'Cyberslav', 'Petrov')
		addMark(self.conn, 'Cyberslav', 'Petrov', math=5, physics=3, russian=2)
		cursor = self.conn.cursor()
		mark = cursor.execute('''SELECT math FROM Student, Marks 
						WHERE Student.id = student_id and name = 'Cyberslav' and lastname = 'Petrov' ''').fetchone()[0]
		self.assertEqual(mark , 5)


if __name__ == "__main__":
	unittest.main()