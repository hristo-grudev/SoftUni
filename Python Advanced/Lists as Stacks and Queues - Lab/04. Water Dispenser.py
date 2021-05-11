from collections import deque

START = 'Start'
END = 'End'
REFILL = 'refill'

water = int(input())

names = deque()

while True:
	command = input()
	if command == START:
		break
	names.append(command)

while True:
	command = input()
	if command == END:
		print(f'{water} liters left')
		break
	if command.startswith(REFILL):
		refill_liters = command.split()[1]
		water += int(refill_liters)
	else:
		person = names.popleft()
		person_liters = int(command)
		if person_liters <= water:
			print(f'{person} got water')
			water -= person_liters
		else:
			print(f'{person} must wait')
