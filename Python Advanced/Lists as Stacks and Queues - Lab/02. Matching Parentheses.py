expression = input()

s = []

for index in range(len(expression)):
	char = expression[index]
	if char == '(':
		s.append(index)
	elif char == ')':
		j = s.pop()
		print(expression[j:index + 1])
