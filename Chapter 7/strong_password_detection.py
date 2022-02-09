# ATBS Ch. 7
# Strong Password Detection
#
# The function 'is_strong_password()' checks if a password is strong by
# matching it against regular expressions, and returns True if it is strong
# and False otherwise. A password is considered strong if it passes the
# following checks:
# 1. It's at least 16 characters in length
# 2. It contains both uppercase and lowercase letters
# 3. It contains at least one digit

import re


def is_strong_password(password: str) -> bool:
	regex_length = re.compile(r'^.{16,}$')
	regex_lowercase = re.compile(r'^.*[a-z].*$')
	regex_uppercase = re.compile(r'^.*[A-Z].*$')
	regex_number = re.compile(r'^.*\d.*$')

	has_16 = bool(regex_length.search(password))
	has_lowercase = bool(regex_lowercase.search(password))
	has_uppercase = bool(regex_uppercase.search(password))
	has_number = bool(regex_number.search(password))

	if has_16 and has_lowercase and has_uppercase and has_number:
		return True
	else:
		return False


test_password = 'Str0ng Passw0rd!'
print(is_strong_password(test_password))
