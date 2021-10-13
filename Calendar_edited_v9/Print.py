import turtle as t
from Calendar import Calendar

# 해당연도 모든 월/날짜 정보를 GUI로 출력 하는 객체 
class Print(Calendar):

	yrcor= [-380,350]
	xcor = [-380, -180, 20, 220]
	ycor = [300, 100, -100, -300]

	def __init__(self, yr):
		super().__init__(yr)

	# Set the Year from Input
	def set_yr_cal(self):
		yr = self.year

		# Initialize Numpy Array 
		cal = Calendar(yr)
		yrcal = cal.get_arr()  
		self.arrCal = yrcal

	## Initialize the Set of turtle
	def set_turt(self):
		s = t.Screen()
		t.listen

		s.setup(width=800, height = 800)
		t.speed("fastest");t.hideturtle()

		t.colormode(255)
		t.pencolor(255,255,255)
		t.bgcolor(30,30,30)

	# Drawing Year
	def draw_turt_yr(self):
		x = self.yrcor[0]
		y = self.yrcor[1]

		t.penup();t.goto(x, y)
		t.write(self.year, font=("맑은고딕", 25,"bold"))  
	
	# Drawing Month
	def draw_turt_mon(self):
		xcor = self.xcor
		ycor = self.ycor

		yrcal = self.arrCal
		cnt=0

		for i in range(3):
			for j in range(4):
				t.penup(); t.goto(xcor[j], ycor[i])
				t.write(yrcal[cnt, 0, 0], font=("맑은고딕", 10, "bold"))  
				cnt+=1

		t.penup(); t.goto(-360, 340)

	# Drawing days
	def draw_turt_day(self,m):
		if m ==12 : return 
		
		x = m %4 
		y = 0 if m < 4 else ( 1 if m < 8 else 2 )

		xcor = self.xcor
		ycor = self.ycor

		weeklen = len(self.arrCal[m,1:])
		up_pos = ycor[y]

		for j in range(weeklen):
			left_pos = xcor[x]
			up_pos -= 20
			for i, txt in enumerate(self.arrCal[m, j + 1]):
				t.penup()
				left_pos += 20
				t.goto(left_pos, up_pos)

				linetxt = "--"
				if txt == linetxt:
					txt = "  "
					t.write(txt, font=("맑은고딕", 10))
				else:
					if i == 0:
						t.pencolor(255,60,60)
						t.write(txt, font=("맑은고딕", 10))
					else:
						if i == 6:
							t.pencolor(95,95,255)
							t.write(txt, font=("맑은고딕", 10))
						else:
							t.pencolor(255,250,250)
							t.write(txt, font=("맑은고딕", 10))
		
		self.draw_turt_day(m+1) # 3중 (함수 밖 1 -안쪽 2) for문 => 재귀로 수정
		t.mainloop()
		
		return 

# if __name__ == '__main__' :