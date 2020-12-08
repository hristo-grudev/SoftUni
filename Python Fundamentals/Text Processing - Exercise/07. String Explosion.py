text = input()

new_string = ''

strength = 0

for i in range(len(text)):
	if strength == 0:
		new_string += text[i]
		if text[i] == '>':
			strength = int(text[i + 1])
	else:
		if text[i] == '>':
			new_string += text[i]
			strength += int(text[i + 1])
		else:
			strength -= 1

print(new_string)
