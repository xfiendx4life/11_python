import unittest
from class_to_test import *

class TestClass_to_test(unittest.TestCase):

	def setUp(self):
		self.cart = ShoppingCart()

	def tearDown(self):
		del self.cart

	def test_add(self):
		self.cart.add({'name':'powerbank', 'price':5000})
		self.assertIn({'name':'powerbank', 'price':5000}, self.cart.items)

	def test_discount(self):
		self.cart.add({'name':'powerbank', 'price':5000})
		self.cart.add({'name':'cellPhone', 'price':10000})
		self.cart.add({'name':'glass', 'price':2000})
		self.cart.add_discount(20)
		self.assertEqual(self.cart.items[1]['price'], 8000)

	def test_get_discount(self):
		self.cart.add({'name':'powerbank', 'price':5000})
		self.cart.add({'name':'cellPhone', 'price':10000})
		self.cart.add({'name':'glass', 'price':2000})
		self.cart.add_discount(10)
		self.assertEqual(self.cart.get_discount(), 'cellPhone')




