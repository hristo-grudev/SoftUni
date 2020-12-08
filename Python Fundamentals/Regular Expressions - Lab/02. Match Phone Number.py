import re
pattern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'
text = input()
matches = re.finditer(pattern, text)
phones = [nii.group() for nii in matches]
print(', '.join(phones))
