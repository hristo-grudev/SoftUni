def input_to_list(count):
	lines = []
	for _ in range(count):
		lines.append(input())

	return lines


def input_to_list_until_command(end_command):
	lines = []
	while True:
		command = input()
		if command == end_command:
			break
		lines.append(command)

	return lines


def is_vip(guest):
	return guest[0].isdigit()


def separate_guests(guests):
	vip_guest = []
	regular_guest = []
	for guest in guests:
		if is_vip(guest):
			vip_guest.append(guest)
		else:
			regular_guest.append(guest)
	return sorted(vip_guest), sorted(regular_guest)


def print_results(guests):
	print(len(guests))
	vip_guest, regular_guest = separate_guests(guests)
	for guest in vip_guest:
		print(guest)
	for guest in regular_guest:
		print(guest)


n = int(input())
reservations = input_to_list(n)
guest_arrived = input_to_list_until_command('END')


# for guest in guest_arrived:
# 	reservations.remove(guest)

guest_not_arrived = set(reservations).difference(set(guest_arrived))

print_results(guest_not_arrived)

