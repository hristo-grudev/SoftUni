def read_matrix():
	data = input()
	rows, cols = map(int, data.split(' '))
	matrix_list = []
	for row in range(rows):
		row_data = list(map(int, input().split(' ')))
		matrix_list.append(row_data)
	return matrix_list


def check_matrix_sum(row, col, matr):
	mat_sum = 0
	for row_index in range(row, row + 3):
		for col_index in range(col, col + 3):
			mat_sum += matr[row_index][col_index]
	return mat_sum


matrix = read_matrix()
# matrix = [
# 	[1, 0, 4, 3, 1, 1],
# 	[1, 3, 1, 3, 0, 4],
# 	[6, 4, 1, 2, 5, 6],
# 	[2, 2, 1, 5, 4, 1],
# 	[3, 3, 3, 6, 0, 5],
# ]
matrix_max_sum = -99999999

matrix_max_dict = {'row': 0, 'col': 0}
for row_index in range(len(matrix) - 2):
	for col_index in range(len(matrix[row_index]) - 2):
		matrix_sum = check_matrix_sum(row_index, col_index, matrix)
		if matrix_sum > matrix_max_sum:
			matrix_max_dict['row'] = row_index
			matrix_max_dict['col'] = col_index
			matrix_max_sum = matrix_sum

print(f'Sum = {matrix_max_sum}')

for row_index in range(matrix_max_dict['row'], matrix_max_dict['row'] + 3):
	print(f"{matrix[row_index][matrix_max_dict['col']]} {matrix[row_index][matrix_max_dict['col'] + 1]} {matrix[row_index][matrix_max_dict['col'] + 2]}")
