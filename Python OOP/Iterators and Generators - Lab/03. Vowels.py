class vowels:

	def __init__(self, string):
		self.string = string
		self.start = 0
		self.all_list = 'AEOUIYaeouiy'
		self.vowels_list = [el for el in self.string if el in self.all_list]

		self.end = len(self.vowels_list) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.start > self.end:
			raise StopIteration
		index = self.start
		self.start += 1
		return self.vowels_list[index]


result = ""
my_string = vowels('Abcedifuty0o')
for char in my_string:
	if char.lower() in ['a', 'e', 'i', 'u', 'y', 'o']:
		result += char + "\n"
