countries = input().split(', ')
capitols = input().split(', ')

capitols_dict = {countries[i]: capitols[i] for i in range(len(countries))}

for key, value in capitols_dict.items():
	print(f'{key} -> {value}')
