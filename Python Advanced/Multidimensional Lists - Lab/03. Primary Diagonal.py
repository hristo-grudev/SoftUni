def read_matrix():
	size = int(input())
	matrix = []
	for row in range(size):
		row_data = list(map(int, input().split(' ')))
		matrix.append(row_data)
	return matrix


def get_primary_diagonal_sum(matrix):
	diagonal_sum = 0
	for i in range(len(matrix)):
		diagonal_sum += matrix[i][i]
	return diagonal_sum


matrix = read_matrix()
results = get_primary_diagonal_sum(matrix)
print(results)
