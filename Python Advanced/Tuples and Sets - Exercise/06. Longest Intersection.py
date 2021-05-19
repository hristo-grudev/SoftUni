def input_to_list(count):
	def make_range(data):
		start, stop = data.split(',')
		sequence = range(int(start), int(stop)+1)
		return sequence

	lines = []
	for _ in range(count):
		fsd, ssd = input().split('-')
		first_seq = make_range(fsd)
		second_seq = make_range(ssd)
		intersection = set(first_seq).intersection(set(second_seq))
		lines.append(intersection)
	return lines


n = int(input())

intersections = input_to_list(n)
longest = sorted(intersections, key=lambda x: -len(x))[0]

print(f'Longest intersection is {list(longest)} with length {len(longest)}')
