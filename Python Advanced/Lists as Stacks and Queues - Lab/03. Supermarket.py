from collections import deque

names_queue = deque()

while True:
	command = input()
	if command == 'End':
		print(len(names_queue))
		break
	elif command == 'Paid':
		while names_queue:
			print(names_queue.popleft())
	else:
		names_queue.append(command)
