from Calendar import Calendar

# 콘솔창 달력 프린트 객체  
class Print_cal(Calendar): # 달력 요일 문자열로 삽입
                      # [" 일"," 월", "화", "수", "목", "금", "토" ]
    month=0

    def __init__(self):
        self.month=1 #(nothing)

    def print_mode(self,mode):

        if mode==1:
            print("전체 달력을 가져옵니다. 연도만 입력하세요: ") 
            yr = int(input())

            cal = Calendar(yr)
            yrcal =cal.get_arr()

            ## 연도만 입력시 ## 전체 연도 달력 출력 ##
            print("--"*8,"%d년"%yr,"--"*8)
            print(yrcal)

            return yrcal

        elif mode==2:
            print("달력을 가져옵니다. 보고 싶은 연도, 해당 월(month)를 입력하세요: ex) 2021 1")
            input_val = [int(i) for i in input().strip().split()]

            yr = input_val[0]
            month = input_val[1] - 1

            cal = Calendar(yr)
            yrcal =cal.get_arr()

            mcal = yrcal[month,:]
            ## 연도, 월 입력시, 해당 월만 출력
            print(mcal)

            return mcal

print("달력 출력 프로그램 입니다. 모드를 선택하세요, 터틀은 2번만 해당 됩니다ㅜ. ")
print("1.해당 연도 달력 전체 보기,    2.해당 월만 보기")
mode = int(input())
p = Print_cal()
p.print_mode(mode)