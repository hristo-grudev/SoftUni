class Smartphone:
	def __init__(self, memory):
		self.memory = memory
		self.memory_taken = 0
		self.apps = []
		self.is_on = False

	def get_memory_left(self):
		return self.memory - self.memory_taken

	def power(self):
		self.is_on = not self.is_on

	def install2(self, app_name, app_memory):
		if app_memory <= self.get_memory_left():
			if self.is_on:
				self.apps.append(app_name)
				self.memory_taken += app_memory
				return f'Installing {app_name}'
			else:
				return f'Turn on your phone to install {app_name}'
		else:
			return f'Not enough memory to install {app_name}'

	def install(self, app_name, app_memory):
		if self.get_memory_left() < app_memory:
			return f'Not enough memory to install {app_name}'

		if not self.is_on:
			return f'Turn on your phone to install {app_name}'

		self.apps.append(app_name)
		self.memory_taken += app_memory
		return f'Installing {app_name}'

	def status(self):
		return f'Total apps: {len(self.apps)}. Memory left: {self.get_memory_left()}'
