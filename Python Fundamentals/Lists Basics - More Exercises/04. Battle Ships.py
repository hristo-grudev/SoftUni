rows = int(input())

filed = []

ships = 0

for nii in range(rows):
	sequence = input().split()
	sequence = [int(i) for i in sequence] 
	ships+=len(sequence)-sequence.count(0)
	filed.append(sequence)


atacks = input().split()

for atack in atacks:
	row=atack.split('-')[0]
	col=atack.split('-')[1]
	filed[int(row)][int(col)]-=1

alived_ships = 0

for row in filed:
	for el in row:
		if el>0:
			alived_ships+=1

print(ships-alived_ships)