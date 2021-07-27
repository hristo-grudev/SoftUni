from .animal import Mammal


class Mouse(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)

	def make_sound(self):
		return "Squeak"


class Dog(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)

	def make_sound(self):
		return "Woof"


class Cat(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)

	def make_sound(self):
		return "Meow"


class Tiger(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)

	def make_sound(self):
		return "ROAR!!!"
