factor = int(input())
count = int(input())

numList = []

for nii in range(1, count+1):
	numList.append(nii*factor)

print(numList)