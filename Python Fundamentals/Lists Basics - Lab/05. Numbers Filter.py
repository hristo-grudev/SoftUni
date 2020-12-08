n = int(input())
numbers = []
filtered = []

for i in range(n):
	currnt_number = int(input())
	numbers.append(currnt_number)

command = input()

if command == "even":
	for number in numbers:
		if number % 2 == 0:
			filtered.append(number)
elif command == "odd":
	for number in numbers:
		if number % 2 != 0:
			filtered.append(number)
elif command == "negative":
	for number in numbers:
		if number< 0:
			filtered.append(number)
elif command == "positive":
	for number in numbers:
		if number >= 0:
			filtered.append(number)

print(filtered)