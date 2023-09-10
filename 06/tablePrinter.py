#!/usr/bin/python3

def printTable(table):
	if type(table) is not list:
		return
	
	cols = [len(max(column, key=len)) + 1 for column in table]

	for i in range(len(table[0])):
		for j in range(len(table)):
			print(table[j][i].rjust(cols[j]), end='')
		print()

if __name__ == "__main__":
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
	
	printTable(tableData)

	
