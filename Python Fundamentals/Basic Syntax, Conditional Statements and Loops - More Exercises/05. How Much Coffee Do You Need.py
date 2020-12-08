word = input()
coffe = 0

words = ['dog', 'cat', 'movie', 'coding']

while word !='END':
	if word.lower() in words:
		if word.isupper():
			coffe += 2
		else:
			coffe+=1
	word = input()

if coffe <6:
	print(coffe)
else:
	print('You need extra sleep')
