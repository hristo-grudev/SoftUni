numbers = list(map(int, input().split(', ')))

max_value = 10

all_groups = []

while len(numbers) != 0:
	gorup = [max_value]
	index = 0
	inex_for_remove = []
	for number in numbers:
		if number<=max_value:
			gorup.append(number)
			inex_for_remove.append(index)
			index-=1
		index+=1
	for ind in inex_for_remove:
		numbers.pop(ind)
	all_groups.append(gorup)
	max_value+=10

for gorup in all_groups:
	print(f"Group of {gorup[0]}'s: {gorup[1:]}")