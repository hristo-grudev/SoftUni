list_of_numbers = map(float, input().split())

numbers_count = {}

for number in list_of_numbers:
	if number not in numbers_count:
		numbers_count[number] = 0
	numbers_count[number] += 1

for number, value in numbers_count.items():
	print(f'{number} - {value} times')
