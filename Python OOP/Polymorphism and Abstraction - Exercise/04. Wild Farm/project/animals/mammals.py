from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)
		self.acceptable_foods = [Vegetable, Fruit]
		self.weight_per_food = 0.1

	def make_sound(self):
		return "Squeak"


class Dog(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)
		self.acceptable_foods = [Meat]
		self.weight_per_food = 0.4

	def make_sound(self):
		return "Woof!"


class Cat(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)
		self.acceptable_foods = [Vegetable, Meat]
		self.weight_per_food = 0.3

	def make_sound(self):
		return "Meow"


class Tiger(Mammal):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight, living_region)
		self.acceptable_foods = [Meat]
		self.weight_per_food = 1

	def make_sound(self):
		return "ROAR!!!"
