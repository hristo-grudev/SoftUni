def sort_numbers(data_list):
	positive_numbers = [el for el in data_list if el >= 0]
	negative_numbers = [el for el in data_list if el < 0]
	return positive_numbers, negative_numbers


data = [int(el) for el in input().split()]

positive_numbers, negative_numbers = sort_numbers(data)

print(sum(negative_numbers))
print(sum(positive_numbers))

if abs(sum(negative_numbers)) > sum(positive_numbers):
	print('The negatives are stronger than the positives')
else:
	print('The positives are stronger than the negatives')
