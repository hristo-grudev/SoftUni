from functools import reduce


def multiply(*args):
	return reduce(lambda x, y: x*y, args)


nums = [float(el) for el in input().split()]
print(multiply(nums))
