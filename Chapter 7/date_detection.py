# ATBS Ch. 7
# Date Detection
#
# The 'vali_date()' function takes a string as an argument and checks if it is
# a valid date in DD/MM/YYYY format. First it uses a simple regex pattern, and
# if a match is found then it performs additional checks to account for
# months with a different number of days and leap years. Finally, the date is
# printed along with a message saying if it is valid or invalid.

import re


def vali_date(date: str) -> None:
	date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

	match = date_regex.search(date)

	if match:
		day = int(match.group(1))
		month = int(match.group(2))
		year = int(match.group(3))

		months_31 = [1, 3, 5, 7, 8, 10, 12]
		months_30 = [4, 6, 9, 11]
		leap_year = year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

		if month in months_31 and day not in range(1, 32):
			valid = False
		elif month in months_30 and day not in range(1, 31):
			valid = False
		elif month == 2 and leap_year and day not in range(1, 30):
			valid = False
		elif month == 2 and not leap_year and day not in range(1, 29):
			valid = False
		else:
			valid = True

		if valid:
			print(f'Valid date: {date}')
		else:
			print(f'Invalid date: {date}')


test_dates = ['31/01/2001', '31/04/2001', '29/02/2004', '29/02/2005']

for d in test_dates:
	vali_date(d)
