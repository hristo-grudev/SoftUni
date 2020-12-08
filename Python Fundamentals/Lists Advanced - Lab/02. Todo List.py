command = input()
notes = [0]*11

while command != 'End':
	tokens = command.split('-')
	priority = int(tokens[0])
	note = tokens[1]
	notes[priority] = note
	command = input()
results = []
for nii in notes:
	if nii != 0:
		results.append(nii)
print(results)