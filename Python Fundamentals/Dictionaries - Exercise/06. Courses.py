from collections import defaultdict
input_data = input()

courses_dict = defaultdict(list)

while input_data != 'end':
	course, student = input_data.split(' : ')
	courses_dict[course].append(student)
	input_data = input()

ordered_courses = sorted(courses_dict.items(), key=lambda x: len(x[1]), reverse=True)

for course in ordered_courses:
	students = sorted(course[1])
	print(f'{course[0]}: {len(students)}')
	for student in students:
		print(f'-- {student}')