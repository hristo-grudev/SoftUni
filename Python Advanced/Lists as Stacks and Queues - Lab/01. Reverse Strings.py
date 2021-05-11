string = input()

arr = []

for char in string:
	arr.append(char)

new_string = ''

while arr:
	new_string += arr.pop()

print(new_string)
