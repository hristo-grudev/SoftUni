import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
text = input()
matches = re.finditer(pattern, text)
numbers = [number.group() for number in matches]
print(' '.join(numbers))