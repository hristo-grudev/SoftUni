import re
pattern = r'\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}'
text = input()
matches = re.finditer(pattern, text)
for nii in matches:
	date = nii.group()
	day = date[0:2]
	month = date[3:6]
	year = date[-4:]
	print(f'Day: {day}, Month: {month}, Year: {year}')