def repeat_text(text, count_str):
	return text * int(count_str)


text = input()
times = input()

try:
	print(repeat_text(text, times))
except ValueError:
	print('Variable times must be an integer')
