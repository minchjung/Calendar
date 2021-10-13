from Print import Print 

def main() :
	print("연도 입력 :")
	year = int(input())
	tut = Print(year) 
	tut.set_yr_cal() 
	tut.set_turt()

	# Print year, month, day
	tut.draw_turt_yr()
	tut.draw_turt_mon()
	tut.draw_turt_day(0)

	return 
main()