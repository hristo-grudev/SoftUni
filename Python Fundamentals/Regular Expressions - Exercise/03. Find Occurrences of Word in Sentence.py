import re
data = input()
searched = input()
pattern = rf'\b{searched}\b'

results = re.findall(pattern, data, re.IGNORECASE)
print(len(results))
