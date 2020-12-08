from collections import defaultdict
number_of_students = int(input())

courses_dict = defaultdict(list)

for _ in range(number_of_students):
	student = input()
	grade = float(input())
	courses_dict[student].append(grade)

sorted_students = sorted(courses_dict.items(), key=lambda x: sum(x[1])/len(x[1]), reverse=True)
for e in sorted_students:
	student = e[0]
	grade = sum(e[1])/len(e[1])
	if grade >= 4.5:
		print(f'{student} -> {grade:.2f}')
