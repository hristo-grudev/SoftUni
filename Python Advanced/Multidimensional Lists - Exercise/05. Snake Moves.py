rows, cols = row_data = list(map(int, input().split()))
word = input()


matrix = []
index_word = 0

for row_index in range(rows):
	matrix.append([0 for el in range(cols)])
	for col_index in range(cols):
		matrix[row_index][col_index] = word[index_word]
		index_word += 1
		if index_word == len(word):
			index_word = 0

for row_index in range(rows):
	if row_index % 2 == 1:
		matrix[row_index].reverse()
	print(''.join(matrix[row_index]))




