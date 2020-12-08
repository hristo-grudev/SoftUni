file_path = input().split('\\')

file_name, file_ext = file_path[-1].split('.')

print(fr'File name: {file_name}')
print(fr'File extension: {file_ext}')
