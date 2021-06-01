def read_matrix(rows):
	matrix_list = []
	for _ in range(rows):
		row_data = input().split()
		matrix_list.append(row_data)
	return matrix_list


def is_valid(pos, rows, cols):
	return 0 <= pos[0] < rows and 0 <= pos[1] <= cols


rows, cols = map(int, input().split())

matrix = read_matrix(rows)
line = input().split()

while not line[0] == 'END':
	if line[0] == 'swap' and len(line) == 5:
		first_el_pos = [int(line[1]), int(line[2])]
		second_el_pos = [int(line[3]), int(line[4])]
		if is_valid(first_el_pos, rows, cols) and is_valid(second_el_pos, rows, cols):
			matrix[first_el_pos[0]][first_el_pos[1]], matrix[second_el_pos[0]][second_el_pos[1]] = \
			matrix[second_el_pos[0]][second_el_pos[1]], matrix[first_el_pos[0]][first_el_pos[1]]
			for row in matrix:
				print(" ".join(row))
		else:
			print('Invalid input!')

	else:
		print("Invalid input!")

	line = input().split()
