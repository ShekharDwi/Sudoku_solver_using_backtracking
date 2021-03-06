import numpy as np
import random


global iniBoard
iniBoard = [[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0]]






def isSafe(board,row,col,num):
	# check row and column for duplicate
	for i in range(9):
		if board[row][i]==num:
			return False
		if board[i][col]==num:
			return False
	#check the sub-grid for duplicate
	X = (row//3)*3
	Y = (col//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if board[X+i][Y+j] == num:
				return False
	#No duplicate found declare safe
	return True			
	
	
def genSudoku():
	global iniBoard
	genBoard = iniBoard
	fills = 0
	pointstofill = 20
	while (fills < pointstofill):
		row = random.randrange(9)
		col = random.randrange(9)
		if (genBoard[row][col] == 0 ):
			n = random.randrange(1,10)
			if isSafe(genBoard,row,col,n):
				genBoard[row][col] = n
				fills += 1
	return genBoard
	
	
	
	
	
board = [[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,0,0]]




def solver(board):
	for row in range(9):
		for col in range(9):
			if board[row][col] == 0:
				for i in range(1,10):
					if isSafe(board,row,col,i):
						board[row][col] = i
						#print("solved at",row,col) #debug purposes
						solver(board)
						board[row][col]=0
						print("backtracking at",row,col)
				return
	print(np.matrix(board))
	input("Next Solution ?")

	
#solver(board)
res = genSudoku()
print(np.matrix(res))
print("\n Solving.... \n")
solved = solver(res)
if solved == None:
	print("catch none ")
print("Solved:")
print(np.matrix(solved))