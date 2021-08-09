from unittest import TestCase, main
from project.mammal import Mammal


class TstMammal(TestCase):
	def setUp(self):
		self.mammal = Mammal("John", "Cat", "Meow")

	def test_init(self):
		self.assertEqual("John", self.mammal.name)
		self.assertEqual("Cat", self.mammal.type)
		self.assertEqual("Meow", self.mammal.sound)
		self.assertEqual("animals", self.mammal._Mammal__kingdom)

	def test_make_sound(self):
		res = self.mammal.make_sound()
		self.assertEqual("John makes Meow", res)

	def test_get_kingdom(self):
		res = self.mammal.get_kingdom()
		self.assertEqual("animals", res)

	def test_info(self):
		res = self.mammal.info()
		self.assertEqual("John is of type Cat", res)


if __name__ == "__main__":
	main()
