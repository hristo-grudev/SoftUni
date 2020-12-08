rooms = int(input())

total_free_chairs = 0
isok = 1

for room in range(1, rooms+1):
	data = input().split()
	chairs = len(data[0])
	people = int(data[1])
	if chairs>=people:
		total_free_chairs+=(chairs-people)
	else:
		isok = 0
		print(f'{abs(chairs-people)} more chairs needed in room {room}')

if isok == 1:
	print(f'Game On, {total_free_chairs} free chairs left')