# ATBS Ch. 3
# The Collatz Sequence
#
# This program asks for an integer and then keeps calling the collatz()
# function on it until it reaches 1

def collatz(number):
	if number % 2 == 0:
		result = number // 2
	else:
		result = 3 * number + 1

	print(result)
	return result


print('Enter an integer:')

while True:
	try:
		num = int(input())
		break
	except ValueError:
		print('You must enter a valid integer.')


while num != 1:
	num = collatz(num)
