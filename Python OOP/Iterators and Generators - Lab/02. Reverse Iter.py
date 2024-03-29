class reverse_iter:

	def __init__(self, iterable_obj):
		self.iterable_obj = iterable_obj
		self.start = len(self.iterable_obj) - 1
		self.end = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.start < 0:
			raise StopIteration
		index = self.start
		self.start -= 1
		return self.iterable_obj[index]


a = reverse_iter([10, 20, 30])

for el in a:
	print(el)
