number_list = [int(num) for num in input().split(', ')]

result = 1

for number in number_list:
	if number <= 5:
		result *= number
	elif number <= 10:
		result /= number

print(result)
