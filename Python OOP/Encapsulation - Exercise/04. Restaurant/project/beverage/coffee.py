from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
	PRICE = 3.5
	MILLILITERS = 50

	def __init__(self, name, caffeine):
		self.__caffeine = caffeine
		super().__init__(name, self.PRICE, self.MILLILITERS)

	@property
	def caffeine(self):
		return self.__caffeine
