numbers = input().split(', ')
beggars = int(input())

arr = [0]*beggars

tempNumbers = numbers.copy()

index = 0
for number in numbers:
	if index==beggars:
		index=0
	arr[index]+=int(number)
	index+=1

print(arr)