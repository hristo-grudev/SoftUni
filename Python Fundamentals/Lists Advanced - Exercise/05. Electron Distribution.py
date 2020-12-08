electrons = int(input())

results = []
cell = 1

while electrons > 0:
	new_el = 2*cell**2
	if new_el>electrons:
		results.append(electrons)
	else:
		results.append(new_el)
	electrons -= new_el
	cell+=1
print(results)