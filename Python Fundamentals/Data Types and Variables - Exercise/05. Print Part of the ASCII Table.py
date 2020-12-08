start = int(input())
end = int(input())

word = ''

for number in range(start, end+1):
	symbol = chr(number)
	word+= (symbol+ ' ')

print(word)