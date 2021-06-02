def func_executor(*args):
	result = []
	for func_name, data in args:
		result.append(func_name(*data))
	return result
