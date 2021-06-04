try:
	with open('test.txt') as file:
		print("File found!")
except FileNotFoundError:
	print("File not found")