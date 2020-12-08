text = input()

new_string = ''

for char in text:
	new_char = chr(ord(char)+3)
	new_string += new_char

print(new_string)
