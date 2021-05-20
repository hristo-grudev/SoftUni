def read_matrix():
	size = int(input())
	matrix_list = []
	for row in range(size):
		row_data = list(map(int, input().split()))
		matrix_list.append(row_data)
	return matrix_list


matrix = read_matrix()

primary_sum = 0
secondary_sum = 0

for i in range(len(matrix)):
	primary_el = matrix[i][i]
	secondary_el = matrix[i][len(matrix) - 1 - i]
	primary_sum += primary_el
	secondary_sum += secondary_el

print(abs(primary_sum - secondary_sum))
