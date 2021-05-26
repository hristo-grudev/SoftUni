n = int(input())

matrix = []
for _ in range(n):
	sub = input().split(', ')
	matrix.append(sub)

new_matrix = [int(el) for row in matrix for el in row]

print(new_matrix)
