def input_to_list(count):
	lines = set()
	for _ in range(count):
		elements = input().split()
		for el in elements:
			lines.add(el)

	return lines


n = input()

data = input_to_list(int(n))

for el in data:
	print(el)
