def check_inside_matrix(row, col):
	if row not in range(n) or col not in range(n):
		return False


def move(row_position, current_col, word, current_row):
	pass


def move_left(current_row, current_col, matrix, word):
	col_position = current_col - 1
	if not check_inside_matrix(current_row, col_position):
		word = word[:-1]
		return current_row, current_col, word
	current_element = matrix[current_row][col_position]
	if current_element != '-':
		word += current_element
	matrix[current_row][col_position] = 'P'
	matrix[current_row][current_col] = '-'
	return current_row, col_position, word


def move_right(current_row, current_col, matrix, word):
	col_position = current_col + 1
	if not check_inside_matrix(current_row, col_position):
		word = word[:-1]
		return current_row, current_col, word
	current_element = matrix[current_row][col_position]
	if current_element != '-':
		word += current_element
	matrix[current_row][col_position] = 'P'
	matrix[current_row][current_col] = '-'
	return current_row, col_position, word


def move_down(current_row, current_col, matrix, word):
	row_position = current_row + 1
	if not check_inside_matrix(row_position, current_col):
		word = word[:-1]
		return current_row, current_col, word
	current_element = matrix[row_position][current_col]
	if current_element != '-':
		word += current_element
	matrix[row_position][current_col] = 'P'
	matrix[current_row][current_col] = '-'
	return row_position, current_col, word


def move_up(current_row, current_col, matrix, word):
	row_position = current_row - 1
	if not check_inside_matrix(row_position, current_col):
		word = word[:-1]
		return current_row, current_col, word
	current_element = matrix[row_position][current_col]
	if current_element != '-':
		word += current_element
	matrix[row_position][current_col] = 'P'
	matrix[current_row][current_col] = '-'
	return row_position, current_col, word


initial_string = input()
n = int(input())

matrix = []

p_row_index = None
p_col_index = None

move_mapper = {
	"left": move_left,
	"right": move_right,
	"down": move_down,
	"up": move_down,
}

for row_index in range(n):
	current_row = list(input())
	if 'P' in current_row:
		p_row_index = row_index
		p_col_index = current_row.index("P")
	matrix.append(list(input()))

n_commands = int(input())

for _ in range(n_commands):
	command = input()
	p_col_index, p_row_index, initial_string = move_mapper[command](p_row_index, p_col_index, matrix, initial_string)

print(initial_string)
for row_index in range(n):
	for col_index in range(n):
		print(''.join(matrix(row_index)))
