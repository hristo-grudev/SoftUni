import re
data = input()

pattern = r'(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-za-z]+\-?[A-Za-z]+(\.[A-Za-z]+)+'

results = re.finditer(pattern, data)
for el in results:
	print((el.group()))
