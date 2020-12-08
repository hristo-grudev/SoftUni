n = int(input())
positives = []
negatives = []

for n in range(n):
	currnt_unmber = int(input())
	if currnt_unmber >=0:
		positives.append(currnt_unmber)
	else:
		negatives.append(currnt_unmber)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')