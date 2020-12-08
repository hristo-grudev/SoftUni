import math
numbers = int(input())

total = 0

for leter in range(numbers):
	letter = input()
	num = ord(letter)
	total+=num

print(f'The sum equals: {total}')