# 정수형 변수와 formatting 을 이용하여 오늘은 2019년 10월 29일 출력하기
year = 2019
month = 10
day = 29
#오류
## print("오늘은 "+year+"년 "+month+"월 "+day+" 일입니다")
### 숫자형을 문자열과 함께 출력하려고 프린트문 쓰면 오류가 난다
# 형변환하여 출력하기
print("오늘은 "+ str(year)+"년 "+str(month)+"월 " + str(day)+" 일입니다.")
#!! 코드가 너무길다
#formatting 하기
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))

#formatting 하기 2
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string,year, month, day+1)