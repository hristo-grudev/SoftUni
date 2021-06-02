def even_odd(*args):
	command_dict = {'odd': 1, 'even': 0}
	numbers = [n for n in args[:-1] if n % 2 == command_dict[args[-1]]]
	return numbers


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
