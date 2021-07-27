from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def __init__(self, name, weight, food_eaten=0):
		self.name = name
		self.weight = weight
		self.food_eaten = food_eaten

	@abstractmethod
	def make_sound(self):
		pass


class Bird(Animal, ABC):
	def __init__(self, name, weight, wing_size):
		super().__init__(name, weight)
		self.wing_size = wing_size


class Mammal(Animal, ABC):
	def __init__(self, name, weight, living_region):
		super().__init__(name, weight)
		self.living_region = living_region
