num = input()

numlist = []
for digit in num:
	numlist.append(digit)

newList = sorted(numlist, reverse = True)

newNum = ''

for nii in newList:
	newNum+=nii

print(newNum)