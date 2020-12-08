start = int(input())

total = 0

for nii in range(start):
	num = int(input())
	if total+num<=255:
		total+=num
	else:
		print('Insufficient capacity!')

print(total)