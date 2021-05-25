def read_matrix():
	data = input()
	rows, cols = map(int, data.split(' '))
	matrix_list = []
	for row in range(rows):
		row_data = input().split(' ')
		matrix_list.append(row_data)
	return matrix_list


matrix = read_matrix()
data = input()


def check_if_index_is_valid(index_row, index_col, rows, cols):
	if 0 <= index_row < rows and 0 <= index_col < cols:
		return True
	return False


def check_if_command_is_valid(command, coordinates, matrix):
	if len(coordinates) == 4 and command == 'swap':
		for index in range(0, len(coordinates), 2):
			if not check_if_index_is_valid(coordinates[index], coordinates[index + 1], len(matrix), len(matrix[0])):
				print('Invalid input!')
				return False
		return True
	print('Invalid input!')
	return False


def print_matrix(matrix):
	for row_index in range(len(matrix)):
		for col_index in range(len(matrix[row_index])):
			print(f'{matrix[row_index][col_index]} ', end='')
		print()


while not data == 'END':
	raw_data = data.split()
	try:
		command = raw_data[0]
		coordinates = [int(el) for el in raw_data[1:]]
	except:
		print('Invalid input!')
	if check_if_command_is_valid(command, coordinates, matrix):
		current_row = coordinates[0]
		current_col = coordinates[1]
		row_to_swap = coordinates[2]
		col_to_swap = coordinates[3]
		temp = matrix[current_row][current_col]
		matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
		matrix[row_to_swap][col_to_swap] = temp
		print_matrix(matrix)

	data = input()
