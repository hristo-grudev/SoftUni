num = int(input())

while True:
	num+=1
	if len(str(num))==len(set(str(num))):
		print(num)
		break