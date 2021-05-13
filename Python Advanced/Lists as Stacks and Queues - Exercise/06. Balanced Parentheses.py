parent = input()
is_balanced = True
openinng = []

mirror = {'{': '}', '[': ']', '(': ')'}

for p in parent:
	if p in '{[(':
		openinng.append(p)
	else:
		if not openinng:
			is_balanced = False
			break
		current_opening_p = openinng.pop()
		if mirror[current_opening_p] != p:
			is_balanced = False
			break

if is_balanced:
	print('YES')
else:
	print('NO')
