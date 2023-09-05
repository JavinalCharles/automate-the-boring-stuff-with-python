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

def isValidChessBoard(chessBoard):
	if type(chessBoard) is not dict:
		return False
	whitePieces = defaultChessPieces()
	blackPieces = defaultChessPieces()
	occupiedTiles = []

	pieces = whitePieces.keys()

	for k, v in chessBoard.items():
		print("checking for piece:", v)
		piece = v[1:]

		# Check if the piece is a valid piece
		if piece not in pieces:
			return False
		if v[0] == 'w':
			whitePieces[piece] += 1
			if piece == 'king':
				if whitePieces[piece] > 1:
					return False
			elif piece == 'pawn':
				if whitePieces[piece] > 8:
					return False
		elif v[0] == 'b':
			blackPieces[piece] += 1
			if piece == 'king':
				if blackPieces[piece] > 1:
					return False
			elif piece == 'pawn':
				if blackPieces[piece] > 8:
					return False
		else: # The prefix is neither 'w' nor 'b'
			return False
		
		# Check the validity of the tile
		rank = k[0]
		file = k[1]
		if not ('1' <= rank and rank <= '8'):
			return False
		if not ('a' <= file and file <= 'h'):
			return False
		if v in occupiedTiles:
			return False
		
		occupiedTiles.append(v)

	if whitePieces['king'] < 1 or blackPieces['king'] < 1:
		return False
	
	if sum(list(whitePieces.values())) > 16 or sum(list(blackPieces.values())) > 16:
		return False
	
	# If execution reaches here, then chessboard must be valid.
	return True


if __name__ == "__main__":
	board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
	pprint.pprint(board1)
	print(isValidChessBoard(board1))

	board2 = {"2h": "brook", "7d": "wpawn", "3h": "bpawn", "8d": "bking", "6e":"wking", "7a": "wbishop"}
	pprint.pprint(board2)
	print(isValidChessBoard(board2))

	board3 = {'9c': 'bking', '8c': 'wqueen', '7d': 'wking'}
	pprint.pprint(board3)
	print(isValidChessBoard(board3))

	board4 = {'1a': 'bking', '8c': 'wqueen', '7d': 'wking', '2a': 'bpawn', '2b': 'bqueen'}
	pprint.pprint(board4)
	print(isValidChessBoard(board4))

	print(isValidChessBoard("hEYO!"))

		
		
