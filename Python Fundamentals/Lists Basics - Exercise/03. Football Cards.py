cards = input().split()

teamA = []
teamB = []

teamAredCards = []
teamBredCards = []

for nii in range(1, 12):
	teamA.append(nii)
	teamB.append(nii)

for nii in cards:
	team = nii.split('-')[0]
	player = nii.split('-')[1]
	if len(teamAredCards) == 5 or len(teamBredCards) == 5:
		break
	if team == 'A':
		if player not in teamAredCards:
			teamAredCards.append(player)
	elif team == 'B':
		if player not in teamBredCards:
			teamBredCards.append(player)

A = len(teamA)-len(teamAredCards)
B = len(teamB)-len(teamBredCards)

print(f'Team A - {A}; Team B - {B}')
if A < 7 or B < 7:
	print('Game was terminated')