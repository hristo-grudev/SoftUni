wolf = input()

wolfList = wolf.split(', ')
wolfList = wolfList[::-1]

if wolfList[0] == 'wolf':
	print('Please go away and stop eating my sheep')
else:
	num = wolfList.index('wolf')
	print(f'Oi! Sheep number {num}! You are about to be eaten by a wolf!')
