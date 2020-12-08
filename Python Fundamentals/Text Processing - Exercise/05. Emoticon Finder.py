text = input()

for i in range(len(text)):
	if text[i] == ':':
		if text[i + 1] != ' ':
			print(f':{text[i + 1]}')

