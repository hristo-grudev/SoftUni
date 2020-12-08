devisor = int(input())
num = int(input())

while True:
	if num%devisor==0:
		print(num)
		break
	num-=1