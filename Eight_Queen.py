from copy import deepcopy
def can_place_queen(temp_board, row, i):
	for j in range(8):
		if(temp_board[j][i] == 'X'): return False
		if((row+j<8) and (i+j<8) and (temp_board[row+j][i+j] == 'X')): return False
		if((row+j<8) and (i-j>=0) and (temp_board[row+j][i-j] == 'X')): return False
		if((row-j>=0) and (i+j<8) and (temp_board[row-j][i+j] == 'X')): return False
		if((row-j>=0) and (i-j>=0) and (temp_board[row-j][i-j] == 'X')): return False
	return True

def place_row(row, temp_board):
	for i in range(8):
		if(can_place_queen(temp_board, row, i)):
			temp_temp_board = deepcopy(temp_board)
			temp_temp_board[row][i] = 'X'
			if(row < 7):
				place_row(row+1, temp_temp_board)
			elif(row == 7):
				global count
				count = count + 1
				for m in range(8):
					for n in range(8):
						print(temp_temp_board[m][n], end="")
					print()
				print(count)

count = 0
board = [[0]*8 for i in range(8)]
place_row(0, board)