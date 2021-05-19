def input_to_list(count):
	even_numbers_set = set()
	odd_numbers_set = set()
	for row in range(1, count+1):
		name = input()
		current_sum = sum([ord(el) for el in name]) // row
		if current_sum % 2 == 0:
			even_numbers_set.add(current_sum)
		else:
			odd_numbers_set.add(current_sum)

	return even_numbers_set, odd_numbers_set


n = int(input())

even_numbers, odd_numbers = input_to_list(n)
sum_evens = sum(even_numbers)
sum_odds = sum(odd_numbers)

if sum_evens == sum_odds:
	modified_set = [str(el) for el in even_numbers.union(odd_numbers)]
	print(f"{', '.join(modified_set)}")
elif sum_odds > sum_evens:
	modified_set = [str(el) for el in odd_numbers.difference(even_numbers)]
	print(f"{', '.join(modified_set)}")
else:
	modified_set = [str(el) for el in odd_numbers.symmetric_difference(even_numbers)]
	print(f"{', '.join(modified_set)}")
