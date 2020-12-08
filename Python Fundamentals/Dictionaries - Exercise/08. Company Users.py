from collections import defaultdict
input_data = input()

company_dict = defaultdict(list)

while input_data != 'End':
	company, employee_id = input_data.split(' -> ')
	if employee_id not in company_dict[company]:
		company_dict[company].append(employee_id)
	input_data = input()

ordered_company = sorted(company_dict.items(), key=lambda x: x)

for company in ordered_company:
	employees = company[1]
	print(f'{company[0]}')
	for employee_id in employees:
		print(f'-- {employee_id}')