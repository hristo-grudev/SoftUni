import datetime


class Time:
	max_hours = 23
	max_minutes = 59
	max_secundes = 59

	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def set_time(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def get_time(self):
		return f'{self.hours:02d} {self.minutes:02d} {self.seconds:02d}'

	def next_second(self):
		new_time = datetime.datetime.strptime(f'{self.hours}:{self.minutes}:{self.seconds}', '%H:%M:%S') + datetime.timedelta(seconds=1)
		str_time = new_time.strftime('')
		return new_time.strftime


time = Time(9, 30, 59)
print(time.get_time())
print(time.next_second())
