# ATBS Ch. 4
# Comma code
#
# The comma_code() function takes a non-empty list as an argument and returns
# a string with the list's values separated by commas and an 'and' before the
# last element.

def comma_code(lst: list):
	if len(lst) == 0:
		print('Error: empty list')
		return None

	result = ''

	if len(lst) > 1:
		for element in lst[:-1]:
			result += str(element) + ', '
		result += 'and '

	result += str(lst[-1])

	return result
