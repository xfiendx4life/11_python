class Item:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		self.discount = False

	def __repr__(self):
		return self.name + ' ' + self.price


class ShoppingCart():

	def __init__(self):
		self.items = []
		self.total_price = 0

	def add_item(self, item):
		self.items.append(item)
		self.total_price += item.price

	def del_item(self, item):
		if item in self.items:
			self.items.remove(item)
			self.total_price -= item.price

	def add_discount(self, discount):
		sorted(self.items, reverse=True, key=lambda item: item.price)
		if not self.items[0].discount:
			self.total_price -= self.items[0].price * discount / 100
			self.items[0].price -= self.items[0].price * discount / 100
			self.items[0].discount = True

	def del_discount(self, discount):
		for i in self.items:
			if i.discount:
				i.discount = False
				i.price /= (1 - discount / 100)
				self.total_price += discount / 100 * i.price


		
