import os
from pathlib import Path


def get_report_for_extensions(files):
	report = {}
	for file in files:
		name, extension = os.path.splitext(file)
		if extension not in report:
			report[extension] = []
		report[extension].append(name)

	return report


dir_content = os.listdir()
files = [el for el in dir_content if '.' in el]
report = get_report_for_extensions(files)
print(report)

result_string = ""

for extension, file_names in sorted(report.items(), key=lambda x: x[0]):
	result_string += f'{extension}\n'
	for name in file_names:
		result_string += f'- - - {name}{extension}\n'


file_name = 'my_report_result.txt'
path_to_desktop = str(Path.home())
with open(os.path.join(path_to_desktop, file_name), 'w') as f:
	f.write(result_string)
