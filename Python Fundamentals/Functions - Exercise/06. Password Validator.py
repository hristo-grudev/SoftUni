password = input()

def check_password(password):
	is_valid = 0
	if len(password) < 6 or len(password) > 10:
		print('Password must be between 6 and 10 characters')
	else:
		is_valid += 1
	if password.isalnum()==False:
		print('Password must consist only of letters and digits')
	else:
		is_valid += 1

	digits = 0
	for nii in password:
		if nii.isdigit():
			digits+=1

	if digits<2:
		print('Password must have at least 2 digits')
	else:
		is_valid += 1

	if is_valid == 3:
		print('Password is valid')


check_password(password)