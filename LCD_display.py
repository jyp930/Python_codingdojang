class draw_line:
	def upper_vertical(pos, s, board):
		for i in range(1, (2*s+3)//2):
			board[i][pos] = '|'
	def lower_vertical(pos, s, board):
		for i in range(((2*s+3)//2)+1, 2*s+2):
			board[i][pos] = '|'
	def horizon(s, i, board, row):
		for i in range(  ((s+2)*i)+1, (s+2)*(i+1)-1  ):
			board[row][i] = '-'	

def ch_LCD_display(s, i, ch, board):
	if(ch in ['2','3','5','6','7','8','9','0']):
		draw_line.horizon(s, i, board, 0)
	if(ch in ['2','3','4','5','6','8','9']):
		draw_line.horizon(s, i, board, (2*s+3)//2)
	if(ch in ['2','3','5','6','8','9','0']):
		draw_line.horizon(s, i, board, 2*s+2)
	if(ch in ['4','5','6','8','9','0']):
		draw_line.upper_vertical((s+2)*(i), s, board)
	if(ch in ['2','6','8','0']):
		draw_line.lower_vertical((s+2)*(i), s, board)
	if(ch in ['1','2','3','4','7','8','9','0']):
		draw_line.upper_vertical((s+2)*(i+1)-1 , s, board)
	if(ch in ['1','3','4','5','6','7','8','9','0']):
		draw_line.lower_vertical((s+2)*(i+1)-1 , s, board)

def LCD_display(s, n):
	n_to_list = list(n)
	index=0 #각 문자의 위치
	board = [[' ']*((s+2)*len(n_to_list)) for i in range(2*s+3)] #전체 display board
	for ch in n_to_list: #한 문자씩 출력
		ch_LCD_display(s, index, ch, board)
		index += 1
	for row in board:
		for el in row:
			print(el, end="")
		print()

#main
while(True):
	s, n = input().split(); s = int(s) #입력구간. s는 display크기, n은 출력할 숫자
	if(s == 0 and n == '0'): break
	LCD_display(s, n) #0 0이 아니면 출력