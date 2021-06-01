def max_number(data_list):
	return max(data_list)


def min_number(data_list):
	return min(data_list)


def sum_number(data_list):
	return sum(data_list)


data = [int(el) for el in input().split()]

print(f'The minimum number is {min_number(data)}')
print(f'The maximum number is {max_number(data)}')
print(f'The sum number is: {sum_number(data)}')
