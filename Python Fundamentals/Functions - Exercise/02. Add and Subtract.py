n1 = int(input())
n2 = int(input())
n3 = int(input())

def sum_numbers(a, b):
	result = a+b
	return result

def substract(a, b):
	result = a-b
	return result

def add_and_substract(a, b, c):
	result = a+b-c
	return result

print(add_and_substract(n1, n2, n3))