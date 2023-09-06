import pprint

def defaultChessPieces():
	return {
		'king': 0,
		'queen': 0,
		'bishop': 0,
		'knight': 0,
		'rook': 0,
		'pawn': 0,
	}

def isValidChessboard(chessBoard):
	if type(chessBoard) is not dict:
		return False
	whitePieces = defaultChessPieces()
	blackPieces = defaultChessPieces()
	occupiedTiles = []

	pieces = whitePieces.keys()

	for k, v in chessBoard.items():
		# print("Evaluating k =", k, "\tv =", v)
		piece = v[1:]

		# Check if the piece is a valid piece
		if piece not in pieces:
			print("Invalid peice")
			return False
		if v[0] == 'w':
			whitePieces[piece] += 1
		elif v[0] == 'b':
			blackPieces[piece] += 1
		else: # The prefix is neither 'w' nor 'b'
			# print("Invalid prefix")
			return False
		
		# Check the validity of the tile
		rank = k[0]
		file = k[1]
		if not ('1' <= rank and rank <= '8'):
			# print("Invalid rank")
			return False
		if not ('a' <= file and file <= 'h'):
			# print("Invalid file")
			return False
		if k in occupiedTiles:
			# print("Doubly-occupied tile")
			return False
		
		occupiedTiles.append(v)

	if whitePieces['king'] != 1 or blackPieces['king'] != 1:
		# print("Either player has king != 1")
		return False
	if whitePieces['pawn'] > 8 or blackPieces['pawn'] > 8:
		# print("Either player has pawn > 8")
		return False
	if sum(list(whitePieces.values())) > 16 or sum(list(blackPieces.values())) > 16:
		# print('Either player has total pieces > 16.')
		return False
	
	# If execution reaches here, then chessboard must be valid.
	return True


if __name__ == "__main__":
	boards = [
		{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'},
		{"2h": "brook", "7d": "wpawn", "3h": "bpawn", "8d": "bking", "6e":"wking", "7a": "wbishop"},
		{'9c': 'bking', '8c': 'wqueen', '7d': 'wking'},
		{'1a': 'bking', '8c': 'wqueen', '7d': 'wking', '2a': 'bpawn', '2b': 'bqueen'},
		"Not a valid chess board at all",
		{'1e': 'wqueen', '1e': 'bbishop'},
		{'2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '4d': 'wpawn', '1d': 'wqueen', '1e': 'wking', '8h': 'brook', '8e': 'bking', '8a': 'bbishop', '1f':'bbishop'},
		{'0d': 'wking', '9d': 'bking'}

	]

	for i, board in enumerate(boards):
		print("Chess Board # ", i, end=":\n")
		pprint.pprint(board)
		print("isValidChessboard():", isValidChessboard(board))
		print("-----------------------------------")


		
		
