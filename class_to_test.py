class ShoppingCart(object):
	
	def __init__(self):
		self.items = []
		self.__total_price = 0

	def add(self, item):
		self.items.append(item)
		self.__total_price += item['price']

	def add_discount(self, discount):
		if self.items != []:
			max_price = 0
			max_n = 0
			for i in range(len(self.items)):
				if self.items[i]['price'] > max_price:
					max_n = i
					max_price = self.items[i]['price']
			self.items[max_n]['price'] = max_price - max_price*discount / 100
			self.items[max_n]['discount'] = True
			self.__total_price -= max_price*discount / 100
		else:
			return False

	def size(self):
		return len(self.items)

	def get_total_price(self):
		return self.__total_price

	def get_discount(self):
		for item in self.items:
			if 'discount' in item.keys():
				return item['name']



		