from Calendar import Calendar
import turtle as t

# 해당년도의 하나의 월/날짜 정보만 GUI로 출력 
class Visual_cal(Calendar):
    mcal=[]

    def __init__(self, yr):
        super().__init__(yr)

    def vis_set_mon(self,month):
        month = month-1
        yr = self.year

        cal = Calendar(yr)
        yrcal=cal.get_arr() # np어레이라 빈어레이로 두고 속성 초기화가 어려워 계속 함수로 생성

        mcal = yrcal[month, :]
        self.arrCal=yrcal

        return mcal
    def vis_print(self,mcal):
        ## 터틀 셋팅
        t.penup()
        t.goto(-410,300)
        t.pendown()
        t.write(mcal[0,0], font = ("맑은고딕",45,"bold")) # 월 표기
        t.hideturtle()
        ## 터틀 월 출력
        up_pos=300
        for j in range(len(mcal[1:])):
            left_pos=-410
            up_pos -= 80
            for i, txt in enumerate(mcal[j+1]):
                t.penup()
                left_pos += 80
                t.goto(left_pos, up_pos)
                t.pendown()

                linetxt = "--"
                if  txt ==linetxt:
                    txt = "  "
                    t.write(txt, font=("맑은고딕", 40))
                else:
                    if i ==0 :
                        t.color("red")
                        t.write(txt, font=("맑은고딕", 40))
                    else:
                        if i==6:
                            t.color("blue")
                            t.write(txt, font=("맑은고딕", 40))
                        else:
                            t.color("black")
                            t.write(txt, font=("맑은고딕", 40))
        t.mainloop()

# vis = Visual_cal(2021) # 연도 입력
# mcal = vis.vis_set_mon(2) # 월 입력
# vis.vis_print(mcal)