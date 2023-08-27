
def printPictureGrid(pictureGrid):
	# I could use "".join(...) here but I think that defeats the point of this practice.
	for y in range(len(pictureGrid)):
		for x in range(len(pictureGrid[y])):
			print(pictureGrid[y][x], end="")
		print()
		


if __name__ == "__main__":
	grid = [
		['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']
	]
	printPictureGrid(grid)