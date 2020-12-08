from collections import defaultdict

resource = defaultdict(int)

res = input()

while res != 'stop':
	qty = int(input())
	resource[res] += qty
	res = input()

for key in resource:
	print(f'{key} -> {resource[key]}')