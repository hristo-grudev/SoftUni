def recursive_power(number, power, result=1):
	if power == 1:
		return number
	return number * recursive_power(number, power - 1, result * number)


print(recursive_power(2, 10))
