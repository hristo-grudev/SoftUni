operator = input()
n1 = int(input())
n2 = int(input())

def solve(a, b, operator):
	if operator == 'multiply':
		return a*b
	elif operator == 'add':
		return a+b
	elif operator == 'subtract':
		return a-b
	elif operator == 'divide':
		return int(a/b)

print(solve(n1, n2, operator))