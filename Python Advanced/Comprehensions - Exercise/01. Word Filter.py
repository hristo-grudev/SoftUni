words = input().split()

data = [print(word) for word in words if len(word) % 2 == 0]
