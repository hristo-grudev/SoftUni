rows, cols = map(int, input().split())


def ascii_to_char(row, columns):
	return [(chr(row + 97) + chr(col + 97 + row) + chr(row + 97)) for col in range(columns)]


def create_matrix(rows, cols):
	matr = [ascii_to_char(row, cols) for row in range(rows)]
	return matr


matrix = create_matrix(rows, cols)

print(*[' '.join(el) for el in matrix], sep='\n')
