number_of_queries = int(input())

s = []

for _ in range(number_of_queries):
	input_command = input().split()
	command = input_command[0]
	if command == '1':
		s.append(int(input_command[1]))
	elif command == '2':
		if s:
			s.pop()
	elif command == '3':
		if s:
			print(max(s))
	elif command == '4':
		if s:
			print(min(s))

print(', '.join([str(el) for el in reversed(s)]))
