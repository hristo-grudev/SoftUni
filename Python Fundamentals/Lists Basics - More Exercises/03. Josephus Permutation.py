sequence = input().split()
counted = int(input())

result = '['

couter = 1
while len(sequence)!=0:
	fordelete = []
	index = 0
	for num in sequence:
		if couter%int(counted)==0:
			result+=num+','
			fordelete.append(index)
		index+=1
		couter+=1

	row=0
	for index in fordelete:
		sequence.pop(index-row)
		row+=1
results = result[:-1]+']'
print(results)