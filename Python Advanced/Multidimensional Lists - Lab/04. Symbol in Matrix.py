def read_matrix():
	size = int(input())
	matrix = []
	for row in range(size):
		row_data = [x for x in input()]
		matrix.append(row_data)
	return matrix


def find_symbol(matrix, symbols):
	for row_index in range(len(matrix)):
		for col_index in range(len(matrix[row_index])):
			current_symbol = matrix[row_index][col_index]
			if current_symbol == symbols:
				return row_index, col_index


def print_results(result):
	if result:
		print(result)
	else:
		print(f'{symbol} does not occur in the matrix')


matrix = read_matrix()
symbol = input()
result = find_symbol(matrix, symbol)
print_results(result)
