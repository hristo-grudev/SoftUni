KING_SYMBOL = "K"
QUEEN_SYMBOL = "Q"


def read_board():
	matrix_list = []
	for row in range(8):
		row_data = input().split()
		matrix_list.append(row_data)
	return matrix_list


def find_king_position(board):
	for row_index in range(len(board)):
		for col_index in range(len(board)):
			if board[row_index][col_index] == KING_SYMBOL:
				return (row_index, col_index)


def in_range(value, max_value):
	return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
	rows_count = len(board)
	cols_count = len(board[0])
	(row_index, col_index) = king
	(delta_row, delta_col) = deltas

	while in_range(row_index, rows_count) and in_range(col_index, cols_count):
		if board[row_index][col_index] == QUEEN_SYMBOL:
			return [row_index, col_index]

		row_index += delta_row
		col_index += delta_col


def get_capturing_queens(board, king):
	deltas = [
		(0, -1),
		(-1, -1),
		(-1, 0),
		(-1, 1),
		(0, 1),
		(1, 1),
		(1, 0),
		(1, -1),
	]

	queens = [
		search_with_deltas(board, king, delta) for delta in deltas
	]
	return [queen for queen in queens if queen]


def print_result(queens):
	if queens:
		for queen in queens:
			print(queen)
	else:
		print('The king is safe!')


matrix = read_board()
king = find_king_position(matrix)
queens = get_capturing_queens(matrix, king)
print_result(queens)
