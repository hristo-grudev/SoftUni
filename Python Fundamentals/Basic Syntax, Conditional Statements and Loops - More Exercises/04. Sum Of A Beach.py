word = input()

lists = ['sand', 'water', 'fish', 'sun']

num = 0

for nii in lists:
	num+=word.lower().count(nii)
print(num)