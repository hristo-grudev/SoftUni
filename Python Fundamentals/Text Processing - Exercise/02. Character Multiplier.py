text = input().split()

pairs = []

for word in text:
	all_char = []
	for char in word:
		all_char.append(ord(char))
	pairs.append(all_char)

pairs = sorted(pairs, key=lambda x: len(x))

total_sum = 0

for index in range(len(pairs[0])):
	total_sum += pairs[0][index] * pairs[1][index]

total_sum += sum(pairs[1][index+1:])

print(total_sum)
