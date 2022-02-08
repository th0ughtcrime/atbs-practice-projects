# ATBS Ch. 5
# Chess Dictionary Validator
#
# The 'is_valid_chessboard()' function takes a dictionary as an argument which
# symbolizes the snapshot of a chessboard, and performs some checks to find if
# the chessboard is valid; then returns 'True' if it's valid and 'False'
# otherwise.
# The dictionary's keys and values symbolize the chessboard's squares and
# pieces, respectively.
#
# A chessboard is considered valid if it passes all the following checks:
# 1. There are exactly 64 squares
# 2. The squares are indexed with all values between 'a1' and 'h8'
# 3. There is exactly one king of each colour
# 4. There is at least 1 and at most 16 pieces of each colour
# 5. All pieces are valid

def is_valid_chessboard(chessboard: dict) -> bool:
	# A valid board is created
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	valid_board = []

	# This for loop creates a 8x8 array containing all valid board indexes.
	# It iterates through the letters normally but through numbers in reverse,
	# so the board is created from White's perspective.
	for row in range(8, 0, -1):
		new_row = []
		for column in letters:
			new_row.append(column + str(row))

		valid_board.append(new_row)

	# A list with all valid pieces is created
	piece_types = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
	piece_colours = ['w', 'b']
	valid_pieces = [c+t for c in piece_colours for t in piece_types]

	# Check 1: There are exactly 64 squares.
	square_count = len(chessboard.keys())
	if square_count != 64:
		return False

	# Check 2: The squares are indexed with all values between 'a1' and 'h8'
	# This for loop iterates through the board that was created above and
	# checks if every board index exists as key in the 'chessboard' dictionary
	for r in range(8):
		for c in range(8):
			if valid_board[r][c] not in chessboard.keys():
				return False

	# Check 3: There is exactly one king of each colour
	board_values = list(chessboard.values())
	king_white = board_values.count('wking')
	king_black = board_values.count('bking')

	if king_black != 1 or king_white != 1:
		return False

	# Check 4: There is at least 1 and at most 16 pieces of each colour
	# Check 5: All pieces are valid pieces
	white_count = 0
	black_count = 0

	for piece in board_values:
		if piece and piece[0] == 'w':
			white_count += 1
		elif piece and piece[0] == 'b':
			black_count += 1

		if piece and piece not in valid_pieces:
			return False

	if white_count not in range(1, 17):
		return False
	elif black_count not in range(1, 17):
		return False

	return True


test_board = {
	'a8':'brook','b8':'bknight','c8':'bbishop','d8':'bqueen','e8':'bking','f8':'bbishop','g8':'bknight','h8':'brook',
	'a7':'bpawn','b7':'bpawn',  'c7':'bpawn',  'd7':'bpawn', 'e7':'bpawn','f7':'bpawn',  'g7':'bpawn',  'h7':'bpawn',
	'a6':'',     'b6':'',       'c6':'',       'd6':'',      'e6':'',     'f6':'',       'g6':'',       'h6':'',
	'a5':'',     'b5':'',       'c5':'',       'd5':'',      'e5':'',     'f5':'',       'g5':'',       'h5':'',
	'a4':'',     'b4':'',       'c4':'',       'd4':'',      'e4':'',     'f4':'',       'g4':'',       'h4':'',
	'a3':'',     'b3':'',       'c3':'',       'd3':'',      'e3':'',     'f3':'',       'g3':'',       'h3':'',
	'a2':'wpawn','b2':'wpawn',  'c2':'wpawn',  'd2':'wpawn', 'e2':'wpawn','f2':'wpawn',  'g2':'wpawn',  'h2':'wpawn',
	'a1':'wrook','b1':'wknight','c1':'wbishop','d1':'wqueen','e1':'wking','f1':'wbishop','g1':'wknight','h1':'wrook'
}

print(is_valid_chessboard(test_board))
