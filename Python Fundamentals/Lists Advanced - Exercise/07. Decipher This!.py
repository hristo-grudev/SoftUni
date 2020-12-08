message = input().split()

new_message = []

for word in message:
	char = [n for n in word if n.isdigit()]
	char = chr(int(''.join(char)))
	word = [n for n in word if not n.isdigit()]
	word = ''.join(word)	
	word = char+word
	word = list(word)
	word[1], word[-1] = word[-1], word[1]
	word = ''.join(word)
	new_message.append(word)

print(' '.join(new_message))