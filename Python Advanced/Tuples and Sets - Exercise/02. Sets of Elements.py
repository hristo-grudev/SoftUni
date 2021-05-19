def input_to_list(count):
	lines = set()
	for _ in range(count):
		lines.add(input())

	return lines

n, m = input().split()

s1 = input_to_list(int(n))
s2 = input_to_list(int(m))

data = s1 & s2

for number in data:
	print(number)
