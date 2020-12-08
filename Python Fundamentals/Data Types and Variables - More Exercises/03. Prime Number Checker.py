a = int(input())

data = "True"

for nii in range(2, a):
	if a%nii==0:
		data = 'False'

print(data)