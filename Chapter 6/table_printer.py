# ATBS Ch. 6
# Table Printer
#
# This program prints a list of strings, right-aligned in a table. The width of
# each column is adjusted based on the length of the words.

def print_table(table: list) -> None:
	column_widths = []

	# This for loop finds the longest word in each row and stores its length in
	# a list, so they can later be used as column widths for the appropriate
	# columns.
	for j in range(len(table)):
		column_widths.append(max([len(word) for word in table[j]]))

	for i in range(len(table[0])):
		for j in range(len(table)):
			print(table[j][i].rjust(column_widths[j]), end=' ')
		print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
