word = input()

capitalList = []

for nii in range(len(word)):
	if word[nii].isupper():
		capitalList.append(nii)
print(capitalList)