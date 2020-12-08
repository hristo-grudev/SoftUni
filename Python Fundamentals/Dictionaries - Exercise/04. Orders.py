from collections import defaultdict

price_dict = defaultdict(int)
qty_dict = defaultdict(int)

products = input()

while products != 'buy':
	product, price, qty = products.split()
	price_dict[product] = float(price)
	qty_dict[product] += int(qty)
	products = input()

for key, value in qty_dict.items():
	print(f'{key} -> {value*price_dict[key]:.2f}')