numbers = input().split(', ')
numbers = [int(x) for x in numbers]

numbers_dict = {'Positive': [n for n in numbers if n >= 0],
                'Negative': [n for n in numbers if n < 0],
                'Even': [n for n in numbers if n % 2 == 0],
                'Odd': [n for n in numbers if n % 2 == 1]}

for key, values in numbers_dict.items():
	values = [str(x) for x in values]
	print(f'{key}: {", ".join(values)}')
