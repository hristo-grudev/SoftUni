from collections import deque


def best_list_pureness(values, k):
	def calculate_pureness(values):
		pureness = 0
		for index, value in enumerate(values):
			pureness += index * value
		return pureness

	values = deque(values)
	k = min(k, len(values))
	best_rotation = 0
	best_pureness = calculate_pureness(values)
	for rotation in range(k + 1):
		current_pureness = calculate_pureness(values)
		if best_pureness < current_pureness:
			best_rotation = rotation
			best_pureness = current_pureness

		# values.appendleft(values.pop())

		values.rotate(1)

	return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
