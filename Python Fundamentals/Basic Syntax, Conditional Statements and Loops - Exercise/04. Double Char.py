word = input()

new_word = ''

for nii in range(len(word)):
	new_word += word[nii] * 2

print(new_word)