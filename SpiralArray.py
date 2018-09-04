#입력 및 matrix 생성
row, column = input().split()
row = int(row)
column = int(column)
mat = [[0]*(column+1) for i in range(row+1)]
for i in range(0,row+1): mat[i][column] = 1
for j in range(0,column+1): mat[row][j] = 1

#계산 부분
i=0; j=0; state=0
for count in range(0,row*column):
	mat[i][j] = count
	if state==0:
		if(mat[i][j+1] == 0):
			j += 1;
		else: i+=1; state=1
	elif state==1:
		if(mat[i+1][j] == 0):
			i += 1;
		else: j-=1; state=2
	elif state==2:
		if(mat[i][j-1] == 0):
				j -= 1;
		else: i-=1; state=3
	elif state==3:
		if(mat[i-1][j] == 0 and i!=1):
			i -= 1;
		else: j+=1; state=0

#출력 부분
for i in range(0,row):
	for j in range(0,column):
		print(mat[i][j], end=" ")
	print()

