def read_matrix():
	data = input()
	rows, cols = map(int, data.split(', '))
	matrix = []
	for row in range(rows):
		row_data = list(map(int, input().split(' ')))
		matrix.append(row_data)
	return matrix


def get_column_sums(matrix):
	sums = []
	for col in range(len(matrix[0])):
		sums.append(0)
		for row in range(len(matrix)):
			sums[-1] += matrix[row][col]
	return sums


def print_results(values):
	[print(x) for x in values]


matrix = read_matrix()
results = get_column_sums(matrix)
print_results(results)
