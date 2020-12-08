import re
data = input()

pattern = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s)|(?=\!)|(?=\.))'
emails = []

while data:
	emails.extend([el.group() for el in re.finditer(pattern, data)])
	data = input()

print(*emails, sep='\n')
