key = int(input())
number = int(input())

string = ''

for nii in range(number):
	letter = input()
	num = ord(letter)
	new_letter = chr(num+key)
	string+=new_letter

print(string)