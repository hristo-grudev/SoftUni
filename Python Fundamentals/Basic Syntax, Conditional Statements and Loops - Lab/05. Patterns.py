number = int(input())

for nii in range(1, number+1):
	print(nii*'*', end='')
	print()

for foo in range(number-1, 0, -1):
	print(foo*'*', end='')
	print()