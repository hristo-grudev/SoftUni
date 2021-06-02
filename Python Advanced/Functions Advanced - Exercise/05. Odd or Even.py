def sum_of_the_numbers(numbers, command):
	command_dict = {'Odd': 1, 'Even': 0}
	even_numbers = [n for n in numbers if n % 2 == command_dict[command]]
	return sum(even_numbers * len(numbers))


command = input()
list_of_numbers = [int(el) for el in input().split()]
print(sum_of_the_numbers(list_of_numbers, command))
