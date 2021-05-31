def convert_to_abs(num_list):
	result = [abs(el) for el in num_list]
	return result


nums = [float(el) for el in input().split()]
print(convert_to_abs(nums))
