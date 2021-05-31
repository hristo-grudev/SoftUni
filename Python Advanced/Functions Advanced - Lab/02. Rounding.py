def round_elements(num_list):
	result = [round(el) for el in num_list]
	return result


nums = [float(el) for el in input().split()]
print(round_elements(nums))
