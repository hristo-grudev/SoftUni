def input_to_list(count):
	lines = set()
	for _ in range(count):
		lines.add(input())

	return lines


n = int(input())

names = input_to_list(n)

for name in names:
	print(name)
