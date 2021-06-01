def read_matrix():
	data = input()
	rows, cols = map(int, data.split())
	matrix_list = []
	for row in range(rows):
		row_data = input().split()
		matrix_list.append(row_data)
	return matrix_list


def check_elements_are_equal(row, col, matr):
	current_element = matr[row][col]
	next_element = matr[row][col + 1]
	element_bottom = matr[row + 1][col]
	element_bottom_right = matr[row + 1][col + 1]
	if current_element == next_element and next_element == element_bottom and element_bottom == element_bottom_right:
		return True
	return False


matrix = read_matrix()
counter = 0
for row_index in range(len(matrix) - 1):
	for col_index in range(len(matrix[row_index]) - 1):
		if check_elements_are_equal(row_index, col_index, matrix):
			counter += 1

print(counter)
