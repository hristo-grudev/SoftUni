def even_numbers(data_list):
	return list(filter(lambda x: x % 2 == 0, data_list))


data = [int(el) for el in input().split()]

print(even_numbers(data))
