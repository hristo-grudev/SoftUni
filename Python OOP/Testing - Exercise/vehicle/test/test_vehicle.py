from unittest import TestCase, main
from project.vehicle import Vehicle


class TstMammal(TestCase):
	def setUp(self):
		self.vehicle = Vehicle(80, 161)

	def test_init(self):
		self.assertEqual(80, self.vehicle.fuel)
		self.assertEqual(80, self.vehicle.capacity)
		self.assertEqual(161, self.vehicle.horse_power)
		self.assertEqual(1.25, self.vehicle.fuel_consumption)

	def test_drive(self):
		self.vehicle.drive(20)
		self.assertEqual(55, self.vehicle.fuel)

	def test_drive_exception_raise(self):
		with self.assertRaises(Exception) as e:
			self.vehicle.drive(100)
		self.assertEqual("Not enough fuel", str(e.exception))

	def test_refuel(self):
		self.vehicle.fuel -= 20
		self.vehicle.refuel(10)
		self.assertEqual(70, self.vehicle.fuel)

	def test_refuel_exception_raise(self):
		with self.assertRaises(Exception) as e:
			self.vehicle.refuel(5)
		self.assertEqual("Too much fuel", str(e.exception))

	def test_str(self):
		self.assertEqual("The vehicle has 161 horse power with 80 fuel left and 1.25 fuel consumption",
		                 str(self.vehicle))


if __name__ == "__main__":
	main()
