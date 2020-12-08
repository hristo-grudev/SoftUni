list1 = input().split(', ')
list2 = input().split(', ')

newlist = [nii for nii in list1 for foo in list2 if nii in foo]

print(sorted(set(newlist), key=newlist.index))