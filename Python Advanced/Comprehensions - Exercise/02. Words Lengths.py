words = input().split(', ')
data = [f'{word} -> {len(word)}' for word in words]
print(', '.join(data))
