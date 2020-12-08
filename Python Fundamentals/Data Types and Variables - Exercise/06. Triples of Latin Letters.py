start = int(input())

first_cahr = 97

for nii in range(first_cahr, first_cahr+start):
	string = ''
	for foo in range(first_cahr, first_cahr+start):
		for boo in range(first_cahr, first_cahr+start):
			print(f'{chr(nii)}{chr(foo)}{chr(boo)}')
