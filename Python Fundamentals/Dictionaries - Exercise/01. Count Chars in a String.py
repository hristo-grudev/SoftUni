from collections import defaultdict

alphabet_dict = defaultdict(int)

text = input()

for a in text:
	if a !=' ':
		alphabet_dict[a] += 1

for key in alphabet_dict.keys():
	print(f'{key} -> {alphabet_dict[key]}')