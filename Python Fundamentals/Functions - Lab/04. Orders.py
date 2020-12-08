data = input()
number = int(input())

def solve(string, times):
	dictPrice = {'coffee': 1.50, 'water': 1.00, 'coke': 1.40, 'snacks': 2.00}
	totalSum = dictPrice[string]*times
	return f'{totalSum:.2f}'

print(solve(data, number))