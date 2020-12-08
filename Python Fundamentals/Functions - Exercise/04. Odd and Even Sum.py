c1 = input()

def sum_odd_even(a):
	odd_sum = 0
	even_sum = 0
	for num in a:
		if int(num)%2==0:
			even_sum+=int(num)
		else:
			odd_sum+=int(num)
	print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')

sum_odd_even(c1)