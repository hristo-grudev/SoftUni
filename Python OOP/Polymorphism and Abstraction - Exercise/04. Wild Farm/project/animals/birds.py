from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
	def __init__(self, name, weight, wing_size):
		super().__init__(name, weight, wing_size)
		self.acceptable_foods = [Meat]
		self.weight_per_food = 0.25

	def make_sound(self):
		return "Hoot Hoot"


class Hen(Bird):
	def __init__(self, name, weight, wing_size):
		super().__init__(name, weight, wing_size)
		self.acceptable_foods = [Vegetable, Fruit, Meat, Seed]
		self.weight_per_food = 0.35

	def make_sound(self):
		return "Cluck"
