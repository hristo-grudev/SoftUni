number = int(input())


def perfect_number(number):
	sum_of_divisors = 0
	for num in range(1, int(number / 2) + 1):
		if number % num == 0:
			sum_of_divisors += num

	if sum_of_divisors == number:
		print('We have a perfect number!')
	else:
		print("It's not so perfect.")


perfect_number(number)