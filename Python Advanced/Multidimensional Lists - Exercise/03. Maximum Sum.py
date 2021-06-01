import sys


def read_matrix():
	data = input()
	rows, cols = map(int, data.split())
	matrix_list = []
	for row in range(rows):
		row_data = list(map(int, input().split()))
		matrix_list.append(row_data)
	return matrix_list



matrix = read_matrix()
# matrix = [
# 	[1, 0, 4, 3, 1, 1],
# 	[1, 3, 1, 3, 0, 4],
# 	[6, 4, 1, 2, 5, 6],
# 	[2, 2, 1, 5, 4, 1],
# 	[3, 3, 3, 6, 0, 5],
# ]
best_sum = -sys.maxsize
best_matrix = []

for row_index in range(len(matrix) - 2):
	for col_index in range(len(matrix[row_index]) - 2):
		sub_matrix = []
		current_sum = 0
		row_counter = 0
		for r in range(row_index, row_index + 3):
			sub_matrix.append([])
			for c in range(col_index, col_index + 3):
				sub_matrix[row_counter].append(matrix[r][c])
				current_sum += matrix[r][c]
			row_counter += 1
		if current_sum >= best_sum:
			best_sum = current_sum
			best_matrix = sub_matrix

print(f'Sum = {best_sum}')

for row in best_matrix:
	print(' '.join([str(x) for x in row]))
