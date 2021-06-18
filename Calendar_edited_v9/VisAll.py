import turtle as t
from Visual_cal import Visual_cal
from Calendar import Calendar
import time 

# 해당연도 모든 월/날짜 정보를 GUI로 출력 하는 객체 
class VisAll(Visual_cal):
    yrcor= [-380,350]
    xcor = [-380, -180, 20, 220]
    ycor = [300, 100, -100, -300]

    def __init__(self, yr):
        super().__init__(yr)

    def set_yr_cal(self):
        yr = self.year

        cal = Calendar(yr)
        yrcal = cal.get_arr()  # np어레이라 빈어레이로 두고 속성 초기화가 어려워 계속 함수로 생성

        self.arrCal = yrcal

    def set_turt(self):
            ## 터틀 셋팅
            s = t.Screen()
            t.listen
            s.setup(width=800, height = 800)
            t.speed("fastest")
            t.colormode(255)
            # t.bgcolor(245,243,197)
    def draw_turt_yr(self):
            x = self.yrcor[0]
            y = self.yrcor[1]

            t.penup()
            t.goto(x, y)
            t.write(self.year, font=("맑은고딕", 25,"bold"))  # 연도

    def draw_turt_mon(self,line):
        y = line
        xcor = self.xcor
        ycor = self.ycor

        yrcal = self.arrCal
        cnt=0
        for i in range(3):
            for j in range(4):
                t.penup()
                t.goto(xcor[j], ycor[i])
                t.color("black")
                t.write(yrcal[cnt, 0, 0], font=("맑은고딕", 10, "bold"))  # 월 표기
                cnt+=1
    def draw_turt_day(self,xline,yline,m):
        yrcal = self.arrCal

        x = xline
        y = yline
        xcor = self.xcor
        ycor = self.ycor

        weeklen = len(yrcal[m,1:])
        up_pos = ycor[y]
        for j in range(weeklen):
            left_pos = xcor[x]
            up_pos -= 20
            for i, txt in enumerate(yrcal[m, j + 1]):
                t.penup()
                left_pos += 20
                t.goto(left_pos, up_pos)

                linetxt = "--"
                if txt == linetxt:
                    txt = "  "
                    t.write(txt, font=("맑은고딕", 10))
                else:
                    if i == 0:
                        t.color("red")
                        t.write(txt, font=("맑은고딕", 10))
                    else:
                        if i == 6:
                            t.color("blue")
                            t.write(txt, font=("맑은고딕", 10))
                        else:
                            t.color("black")
                            t.write(txt, font=("맑은고딕", 10))
start = time.time() 
t.hideturtle()
t.speed(0)
tut = VisAll(333) # 연도 입력
tut.set_yr_cal() #
tut.set_turt()
tut.draw_turt_yr()

# 터틀 달력 출력 
for j in range(3):
    tut.draw_turt_mon(j)

t.penup()
t.goto(-360,340)

m=0
for j in range(3):
    for i in range(4):
        tut.draw_turt_day(i,j,m)
        m+=1
t.mainloop()
end = time.time() 
print(end - start )