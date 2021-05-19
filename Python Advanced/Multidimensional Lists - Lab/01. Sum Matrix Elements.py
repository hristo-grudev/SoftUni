def read_matrix():
	data = input()
	rows, cols = map(int, data.split(', '))
	matrix = []
	for row in range(rows):
		row_data = list(map(int, input().split(', ')))
		matrix.append(row_data)
	return matrix


matrix = read_matrix()

matrix_sum = 0
for row in range(len(matrix)):
	r = matrix[row]
	row_sum = 0
	for col in range(len(r)):
		row_sum += r[col]

	matrix_sum += row_sum

print(matrix_sum)
print(matrix)
