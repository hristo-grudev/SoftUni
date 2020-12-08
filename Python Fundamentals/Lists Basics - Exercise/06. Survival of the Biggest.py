numbers = input().split()
delete = int(input())

intNumbers = []

for number in numbers:
	intNumbers.append(int(number))

for nii in range(delete):
	intNumbers.remove(min(intNumbers))

print(intNumbers)