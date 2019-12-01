from cl import *
import unittest

class TestCart(unittest.TestCase):

	def setUp(self):
		self.sc = ShoppingCart()

	def tearDown(self):
		del self.sc

	def testAddItem(self):
		i1 = Item('pizza', 400)
		self.sc.add_item(i1)
		self.assertIn(i1, self.sc.items)

	#@unittest.expectedFailure
	def testDelItem(self):
		i1 = Item('pizza', 400)
		i2 = Item('burger', 250)
		self.sc.add_item(i1)
		self.sc.add_item(i2)
		self.sc.del_item(i1)
		self.assertNotIn(i1, self.sc.items)

	def testAddDiscount(self):
		i1 = Item('pizza', 400)
		i2 = Item('burger', 250)
		self.sc.add_item(i1)
		self.sc.add_item(i2)
		self.sc.add_discount(10)
		self.assertEqual(self.sc.items[0].price, 360)

	def testAddDiscount1(self):
		i1 = Item('pizza', 400)
		i2 = Item('burger', 250)
		self.sc.add_item(i1)
		self.sc.add_item(i2)
		self.sc.add_discount(10)
		self.assertTrue(self.sc.items[0].discount)

	def testDelDiscount(self):
		i1 = Item('pizza', 400)
		i2 = Item('burger', 250)
		self.sc.add_item(i1)
		self.sc.add_item(i2)
		self.sc.add_discount(10)
		self.sc.del_discount(10)
		self.assertFalse(self.sc.items[0].discount)

	def testDelDiscount1(self):
		i1 = Item('pizza', 400)
		i2 = Item('burger', 250)
		self.sc.add_item(i1)
		self.sc.add_item(i2)
		self.sc.add_discount(10)
		self.sc.del_discount(10)
		self.assertEqual(self.sc.items[0].price, 400)

if __name__ == "__main__":
	unittest.main(failfast=True)