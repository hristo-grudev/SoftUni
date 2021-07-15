class ProductRepository:
	def __init__(self):
		self.products = []

	def add(self, product):
		self.products.append(product)

	def find(self, product_name):
		for p in self.products:
			if p.name == product_name:
				return p

	def remove(self, product_name):
		p = self.find(product_name)
		if p:
			self.products.remove(p)

	def __repr__(self):
		result = [f'{p.name}: {p.quantity}' for p in self.products]
		return '\n'.join(result)
