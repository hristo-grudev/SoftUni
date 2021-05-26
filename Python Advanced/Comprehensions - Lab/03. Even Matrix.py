n = int(input())

matrix = []
for _ in range(n):
	sub = input().split(', ')
	matrix.append(sub)

new_matrix = [[int(el) for el in row if int(el) % 2 == 0] for row in matrix]

print(new_matrix)
