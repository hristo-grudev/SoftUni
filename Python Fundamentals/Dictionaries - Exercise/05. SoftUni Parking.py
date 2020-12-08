registered_users = {}

number_of_users = int(input())

for _ in range(number_of_users):
	data = input().split()
	action = data[0]
	username = data[1]
	try:
		license_number = data[2]
	except:
		pass
	if action == 'register':
		if username not in registered_users.keys():
			registered_users[username] = license_number
			print(f'{username} registered {license_number} successfully')
		else:
			print(f'ERROR: already registered with plate number {license_number}')
	elif action == 'unregister':
		if username in registered_users.keys():
			del registered_users[username]
			print(f'{username} unregistered successfully')
		else:
			print(f'ERROR: user {username} not found')

for username, number in registered_users.items():
	print(f'{username} => {number}')