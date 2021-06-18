import numpy as np

# 3달뒤 돌아보는 Self review comment == 
# 생성자 내에서 내부 함수를 모두 호출해서, 필드를 Setting 하고 있다.  
# 이때는 연도만 외부에서 입력받고 모든게 일괄 처리 되야 했기 때문에 이런식으로 작성 했는 듯 하다.  
# 그렇더라도 Setter를 외부적으로 작동 시키는 방향으로 Refactoring 이 필요해 보인다.
# 즉 외부에서 객체를 생성하고, 다시 외부에서 값을 Setting 하는 방식이 적절해 보인다.  
# 그리고, numpy를 연습해보려고 3차원 객체로 구성했는데, tutle로 달력 UI 구현시 굉장히 번거롭고 어려워진다.   
# Remind that 단순함이 재사용하기 좋다!! 
class Calendar:
    # 기본 속성 by 생성자 w 함수
    year = 1
    checker = 1
    addCnt = 0
    # setter로 속성 설정
    firstWeek_list = []
    ref_endList = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365] # 윤년이 아닌 년도의 매달 끝 누적 day
    # ref_endList 윤년이면 2월부터 +1로 세팅

    # getter로 속성 설정 and return
    calendar=[] # 2차원 리스트 달력
    # arrCal=[] # 3차원 어레이 달력 [numpy]

    def __init__(self, yr):  # 생성자
        self.year = yr  # 연도 변경
        self.yrChecker()  # 윤년 체크
        self.addDays()  # 윤년 횟수
        self.set_firstWeek(self.addCnt) # 첫째주 설정 함수 호출
        self.set_ref_endList(self.checker) # 각 달의 마지막날 설정 함수 호출
        self.get_calendar() #  달력 생성 함수 호출
        # self.get_arr()
        # 상속 클래스에서 super 생성자로 모두 한번에 설정

          
    def yrChecker(self):  # yr가 윤년인지 체크 setter
        checker = self.checker
        yr = self.year
        if yr % 4 == 0:
            if yr % 100 == 0:
                if yr % 400 == 0:
                    checker = 2
                else:
                    checker = 1
            else:
                checker = 2  # 윤년이면 checker=2
        self.checker = checker  # 속성 값 변경

    # 1년~ yr전 까지 윤년 횟수 카운트
    def addDays(self):  # setter
        yr = self.year
        cnt = 0
        for y in range(1, yr):  # (355+1에서 +1이 몇번인지 count)
            if y % 4 == 0:
                if y % 100 == 0:
                    if y % 400 == 0:
                        cnt += 1
                else:
                    cnt += 1  # 해당yr 전까지 총 윤년 횟수
        print(cnt)
        self.addCnt = cnt  # 속성값 변경

    def set_firstWeek(self, cnt):  # yr 1월1일이 요일 셋팅
        addDays = ((365 * self.year) + cnt) % 7
        print(addDays)
        temp = [0 for i in range(addDays)] # 1월 첫째주 0 추가

        self.firstWeek_list = temp # 일 월 화 수 목 금 토

    def set_ref_endList(self, checker):  # 윤년이면 366일로 셋팅
        temList = self.ref_endList
        if checker != 1:  # 2월 이후 마지막날 +1
            temList = [i if i == 31 else i + 1 for i in temList]

        self.ref_endList = temList  

    def get_calendar(self):  # 달력 만들기 <- 넘파이 어레이 맞추기 위해 ...삽질 ㅠ
        calendar = []
        eDay = self.ref_endList

        forJan = self.firstWeek_list  # 1월의 첫번째 week 설정 by 0추가된 firstweek_List
        forJan.extend(range(1, 32))
        while len(forJan) % 7 != 0: # 마지막주 0추가 <-7의 배수로 set
            forJan.append(0)
        calendar.append(forJan)

        for i, d in enumerate(eDay):  # 매달 요일 설정 <-각월의 길이 7의 배수로 끝날 수 있게 0을 추가
            if i != 0: # 1월 빼고
                if 0 in calendar[i - 1][10:]:# 2월이후 첫 주 요일 설정
                    zeroes = calendar[i - 1][10:].count(0) # 전 달의 마지막 0 카운트 후
                    firstWeek = len(calendar[i - 1][:-zeroes]) % 7  # 첫 주 0 추가
                    temp = [0 for i in range(firstWeek)] 
                    temp.extend(range(1, d - eDay[i - 1] + 1)) # 0 +  해당 월 날짜 설정
                    # ref_endList= eDay: [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

                    while len(temp) % 7 != 0: # 끝주 7배수
                        temp.append(0)
                    calendar.append(temp)

                else: # 전 달이 7배수로 딱 떨어지면
                    temp = [i for i in range(1, d - eDay[i - 1] + 1)] # 그냥 날짜만 설정

                    while len(temp) % 7 != 0: # 끝주 7배수
                        temp.append(0)
                    calendar.append(temp)
                    # print(calendar)
        self.calendar=calendar # 2차원 리스트 달력

    def get_arr(self):  # 3차원 어레이 달력
        calendar=self.calendar # 달력 속성값 상속
        lengMon = []
        for i, cal in enumerate(calendar):
            lengMon.append(len(cal))

        maxLeng = max(lengMon)
        for i, cal in enumerate(calendar):
            if len(cal) < maxLeng:
                tem = [0 for i in range(maxLeng - len(cal))]
                cal.extend(tem)

        newCalendar=[] # 요일 삽입 된 달력 ,
        for i,mon in enumerate(calendar): # 어레이 타입을 문자열로 맞추기
            month_name = ["*", "*", "*", "*", "*", "*"] # 콘솔창 출력용
            tem_mon= [str(i+1)+ "월    "]
            dayList = ["일","월", "화", "수", "목", "금", "토" ] # 요일 배열 추가
            month_name=tem_mon+month_name+dayList
            for j,day in enumerate(mon): # int ->str로 변환
                if day==0:
                    day = "--" # 0을 --로 변환
                    calendar[i][j]=day
                else:
                    if day<10:
                        day="0"+str(day) # 자리수 두자리로 set
                        calendar[i][j]=day
                    else:
                        day=str(day)
                        calendar[i][j]=day
            month_name=month_name+calendar[i]
            newCalendar.append(month_name)
        arrCal = np.reshape(newCalendar, (12, 2+int(maxLeng / 7), 7) )  # 3차원 배열 설정
        self.arrCal = arrCal

        return arrCal  # 달력
# yr = Calendar(2021)
# arrCal = yr.get_arr()