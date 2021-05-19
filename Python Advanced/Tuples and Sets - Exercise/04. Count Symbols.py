text = input()

char_dict = {}

for char in text:
	if char not in char_dict:
		char_dict[char] = 1
	else:
		char_dict[char] += 1

sorted_data = sorted(list(char_dict.keys()))

for char in sorted_data:
	print(f'{char}: {char_dict[char]} time/s')
