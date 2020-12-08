string = input()

stringList = string.split()

new_list = []

for nii in stringList:
	new_list.append(int(nii)*(-1))

print(new_list)