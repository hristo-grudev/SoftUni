from .operations import add, subtract, divide, multiply, power


def calculate_expression(expression):
	(x, sign, y) = expression.split()
	x = float(x)
	y = int(y)
	sign_dict = {'+': add, '-': subtract, '*': multiply, '/': divide, '^': power}

	return sign_dict[sign](x, y)
