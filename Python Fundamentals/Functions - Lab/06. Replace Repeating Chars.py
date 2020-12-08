text = input()

grouped_text = ' '

for char in text:
	if grouped_text[-1] != char:
		grouped_text += char
print(grouped_text.strip())
