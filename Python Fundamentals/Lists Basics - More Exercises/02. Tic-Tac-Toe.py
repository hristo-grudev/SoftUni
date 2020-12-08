firstline = input().split()
secondline = input().split()
thirdline = input().split()

dictPlayers = {'1': 'First', '2': 'Second'}

if len(list(set(firstline))) == 1 and firstline[0] != '0':
	player = dictPlayers[firstline[0]]
	print(f'{player} player won')
elif len(list(set(secondline))) == 1 and secondline[0] != '0':
	player = dictPlayers[secondline[0]]
	print(f'{player} player won')
elif len(list(set(thirdline))) == 1 and thirdline[0] != '0':
	player = dictPlayers[thirdline[0]]
	print(f'{player} player won')
elif firstline[0] == secondline[1] == thirdline[2] and firstline[0] != '0':
	player = dictPlayers[firstline[0]]
	print(f'{player} player won')
elif firstline[2] == secondline[1] == thirdline[0] and thirdline[0] != '0':
	player = dictPlayers[firstline[2]]
	print(f'{player} player won')
elif firstline[0] == secondline[0] == thirdline[0] and firstline[0] != '0':
	player = dictPlayers[firstline[0]]
	print(f'{player} player won')
elif firstline[1] == secondline[1] == thirdline[1] and firstline[1] != '0':
	player = dictPlayers[firstline[1]]
	print(f'{player} player won')
elif firstline[2] == secondline[2] == thirdline[2] and firstline[2] != '0':
	player = dictPlayers[firstline[2]]
	print(f'{player} player won')
else:
	print('Draw!')