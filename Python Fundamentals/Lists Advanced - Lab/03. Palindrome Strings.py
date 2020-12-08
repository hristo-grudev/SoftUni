string = input().split(' ')
s_pal = input()
pal = []

for word in string:
	if word == ''.join(reversed(word)):
		pal.append(word)

print(f'{pal}')
print(f'Found palindrome {pal.count(s_pal)} times')