n = int(input())

names = []

for _ in range(n):
	name = input()
	names.append(name)


unique_names = set()
for name in names:
	unique_names.add(name)

for name in unique_names:
	print(name)
