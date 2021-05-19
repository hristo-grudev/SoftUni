def input_to_list_until_command():
	def input_to_list(count, data):
		lines = []
		for _ in range(count):
			key = input()
			try:
				lines.append(f'{key} -> {data[key]}')
			except:
				lines.append(f'Contact {key} does not exist.')

		return lines

	lines_dict = {}
	while True:
		command = input()
		if command.isdigit():
			s = input_to_list(int(command), lines_dict)
			break
		name, number = command.split('-')
		lines_dict[name] = number

	return s


data = input_to_list_until_command()
for name in data:
	print(name)
