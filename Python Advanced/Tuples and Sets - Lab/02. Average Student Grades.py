number_of_records = int(input())

students_grades = {}

for _ in range(number_of_records):
	name, grade = input().split()
	grade = float(grade)
	if name not in students_grades:
		students_grades[name] = []
	students_grades[name].append(grade)

for student, grades in students_grades.items():
	grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
	avg_grade = sum(grades)/len(grades)
	print(f'{student} -> {grades_string} (avg: {avg_grade:.2f})')
