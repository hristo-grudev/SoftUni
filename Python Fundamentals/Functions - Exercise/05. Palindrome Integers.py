c1 = input().split(', ')

def sum_odd_even(a):
	for nii in a:
		if nii==nii[::-1]:
			print('True')
		else:
			print('False')

sum_odd_even(c1)