numbers = input().split(', ')

newList = []

zero = 0

for number in numbers:
	if number=='0':
		zero+=1
	else:
		newList.append(int(number))

for o in range(zero):
	newList.append(0)

print(newList)