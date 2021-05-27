size = int(input())

matrix = []

for _ in range(size):
	matrix.append(input().split(', '))

first_diagonal_elements = []
second_diagonal_elements = []

first_diagonal_sum = 0
second_diagonal_sum = 0

for i in range(size):
	first_diagonal_elements.append(matrix[i][i])
	second_diagonal_elements.append(matrix[i][size - 1 - i])
	first_diagonal_sum += int(matrix[i][i])
	second_diagonal_sum += int(matrix[i][size - 1 - i])

print(f'First diagonal: {", ".join(first_diagonal_elements)}. Sum: {first_diagonal_sum}')
print(f'Second diagonal: {", ".join(second_diagonal_elements)}. Sum: {second_diagonal_sum}')
