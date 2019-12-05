import unittest
from funcs import *
import sqlite3

class Test_db(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("mtm.db")


	def tearDown(self):
		cursor = self.conn.cursor()
		cursor.execute('DELETE FROM Child')
		cursor.execute('DELETE FROM Parent')
		cursor.execute('DELETE FROM Parent_child_table')
		self.conn.commit()
		self.conn.close()

	def testAddParent(self):
		self.assertTrue(addParent(self.conn, 'Cyberslava', 'Ukraine'))

	def testAddParentQuery(self):
		addParent(self.conn, 'Cyberslava', 'Ukraine')
		cursor = self.conn.cursor()
		res = cursor.execute("SELECT * FROM Parent WHERE name = 'Cyberslava'").fetchone()	
		self.assertTrue(res)

	def testAddChild(self):
		self.assertTrue(addChild(self.conn, 'Cybergeroyam', 'Slava'))

	def testAddChildQuery(self):
		addChild(self.conn, 'Cybergeroyam', 'Slava')
		cursor = self.conn.cursor()
		res = cursor.execute("SELECT * FROM Child WHERE name = 'Cybergeroyam'").fetchone()	
		self.assertTrue(res)

	def testConnection(self):
		addParent(self.conn, 'Cyberpacan', 'Cyberchetkiy')
		addChild(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')
		self.assertTrue(addConnection(self.conn, 'Cyberpacan', 'Cyberchetkiy',  'Cyberpacanchik', 'Cyberchetkiy'))

	def testConnectionQuery(self):
		addParent(self.conn, 'Cyberpacan', 'Cyberchetkiy')
		addChild(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')
		addConnection(self.conn, 'Cyberpacan', 'Cyberchetkiy',  'Cyberpacanchik', 'Cyberchetkiy')
		cursor = self.conn.cursor()
		res = cursor.execute('''SELECT * FROM Parent_child_table 
						WHERE child_id = (SELECT id FROM Child WHERE name = ? and lastname = ?) and 
						parent_id =  (SELECT id FROM Parent WHERE name = ? and lastname = ?) ''', 
						('Cyberpacanchik', 'Cyberchetkiy', 'Cyberpacan', 'Cyberchetkiy')).fetchone()
		self.assertTrue(res)

	def testGetParents(self):
		addParent(self.conn, 'Cyberpacan', 'Cyberchetkiy')
		addChild(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')
		addConnection(self.conn, 'Cyberpacan', 'Cyberchetkiy',  'Cyberpacanchik', 'Cyberchetkiy')
		self.assertTrue(getAllParents(self.conn, 'Cyberpacanchik', 'Cyberchetkiy'))

	def testGetParentsName(self):
		addParent(self.conn, 'Cyberpacan', 'Cyberchetkiy')
		addChild(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')
		addConnection(self.conn, 'Cyberpacan', 'Cyberchetkiy',  'Cyberpacanchik', 'Cyberchetkiy')
		self.assertEqual(getAllParents(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')[0][1], 'Cyberpacan')

	def testGetChildren(self):
		addParent(self.conn, 'Cyberpacan', 'Cyberchetkiy')
		addChild(self.conn, 'Cyberpacanchik', 'Cyberchetkiy')
		addConnection(self.conn, 'Cyberpacan', 'Cyberchetkiy',  'Cyberpacanchik', 'Cyberchetkiy')
		self.assertEqual(getAllChildren(self.conn, 'Cyberpacan', 'Cyberchetkiy')[0][1], 'Cyberpacanchik')


if __name__=='__main__':
	unittest.main(failfast = True)