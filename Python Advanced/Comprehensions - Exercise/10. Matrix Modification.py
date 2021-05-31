def read_matrix():
	matrix_size = int(input())
	matr = [[int(i) for i in input().split()] for _ in range(matrix_size)]
	return matr


matrix = read_matrix()
input_data = input().split()
command = input_data[0]

while command != 'END':
	command = input_data[0]
	row = int(input_data[1])
	col = int(input_data[2])
	value = int(input_data[3])
	if row not in range(0, len(matrix)) or col not in range(0, len(matrix)):
		print('Invalid coordinates')
	else:
		if command == 'Add':
			matrix[row][col] += value
		elif command == 'Subtract':
			matrix[row][col] -= value

	input_data = input().split()
	command = input_data[0]

[print(*el) for el in matrix]
