#좌표는 list로 표현된다
#rec은 직사각형을 표현하는 객체이다
class rec:
	def __init__(self, x1, y1, x2, y2):
		self.left_down = [x1, y1]
		self.right_up = [x2, y2]
	def set_position(self, x1, y1, x2, y2):
		self.left_down = [x1, y1]
		self.right_up = [x2, y2]
	def get_left_down(self):
		return self.left_down
	def get_right_up(self):
		return self.right_up
	def get_x1(self):
		return self.left_down[0]
	def get_x2(self):
		return self.right_up[0]
	def get_y1(self):
		return self.left_down[1]
	def get_y2(self):
		return self.right_up[1]	

#두 선분의 intersection을 구한다.
def two_line_intersection(line1, line2):
	if(line1[0] > line2[0]): line1, line2 = line2, line1 #선분 sort
	if(line1[1] <= line2[0]): return None #겹치지 않음
	else: #겹침
	 if(line1[1] >= line2[1]): #포함
	 	return line2
	 else: #포함은 안하지만 겹침
	 	return [line2[0], line1[1]]

#두 사각형의 intersection을 구한다
#(x좌표끼리의 intersection) and (y좌표끼리의 intersection)
def two_rec_intersection(rec1, rec2):
	#x좌표끼리의 intersection 구하기
	x_line1 = [rec1.get_x1(), rec1.get_x2()]
	x_line2 = [rec2.get_x1(), rec2.get_x2()]
	x_result = two_line_intersection(x_line1, x_line2)
	if(x_result is None): #겹치지 않음
		return rec(0,0,0,0)
	#y좌표끼리의 intersection 구하기
	y_line1 = [rec1.get_y1(), rec1.get_y2()]
	y_line2 = [rec2.get_y1(), rec2.get_y2()]
	y_result = two_line_intersection(y_line1, y_line2)
	if(y_result is None): #겹치지 않음
		return rec(0,0,0,0)
	#겹치면
	return rec(x_result[0], y_result[0], x_result[1], y_result[1])

#직사각형의 넓이를 구한다
def square(rec1):
	return (rec1.get_x2()-rec1.get_x1())*(rec1.get_y2()-rec1.get_y1())

#이제부터 Main
#직사각형 4개 입력
coor = list(map(int, input().split()))
rec1 = rec(coor[0], coor[1], coor[2], coor[3])
coor= list(map(int, input().split()))
rec2 = rec(coor[0], coor[1], coor[2], coor[3])
coor = list(map(int, input().split()))
rec3 = rec(coor[0], coor[1], coor[2], coor[3])
coor = list(map(int, input().split()))
rec4 = rec(coor[0], coor[1], coor[2], coor[3])

#넓이 계산
result = 0
rec1_2 = two_rec_intersection(rec1, rec2)
rec1_3 = two_rec_intersection(rec1, rec3)
rec1_4 = two_rec_intersection(rec1, rec4)
rec2_3 = two_rec_intersection(rec2, rec3)
rec2_4 = two_rec_intersection(rec2, rec4)
rec3_4 = two_rec_intersection(rec3, rec4)

rec1_2_3 = two_rec_intersection(rec1, rec2_3)
rec1_2_4 = two_rec_intersection(rec1, rec2_4)
rec1_3_4 = two_rec_intersection(rec1, rec3_4)
rec2_3_4 = two_rec_intersection(rec2, rec3_4)

rec1_2_3_4 = two_rec_intersection(rec1, rec2_3_4)

result = square(rec1) + square(rec2) + square(rec3) + square(rec4) - square(rec1_2) - square(rec1_3) - square(rec1_4) - square(rec2_3) - square(rec2_4) - square(rec3_4) + square(rec1_2_3) + square(rec1_2_4) + square(rec1_3_4) + square(rec2_3_4) - square(rec1_2_3_4)

print(result)