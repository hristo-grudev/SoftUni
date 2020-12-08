number = int(input())

s1 = 0
s2 = 0

stringCheck =''
mark = 0

for nii in range(number):
	string=input()
	if string=='(':
		s1+=1
		if stringCheck==string:
			mark=1
		stringCheck = string


	elif string==')':
		s2+=1
		stringCheck = string

if s1==s2 and stringCheck == ')' and mark==0:
	print('BALANCED')
else:
	print('UNBALANCED')