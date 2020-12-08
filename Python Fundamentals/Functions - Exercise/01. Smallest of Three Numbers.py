n1 = int(input())
n2 = int(input())
n3 = int(input())

def solve(a, b, c):
	result = min([int(a), int(b), int(c)])
	return result

print(solve(n1, n2, n3))
