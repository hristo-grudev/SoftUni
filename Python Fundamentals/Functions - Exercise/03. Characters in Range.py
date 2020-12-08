c1 = input()
c2 = input()

def between_char(a, b):
	first = ord(a)
	last = ord(b)
	for char in range(first+1, last):
		print(chr(char), end=' ')

between_char(c1, c2)