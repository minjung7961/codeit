# input 함수를 실습해보자
name = input("이름을입력하세요")
print(name)

# input 은 값을 받아 무조건 프로그램에 string 값으로 반환한다 그래서 정수를 연산할때는 이렇게 해야한다
num = int(input("숫자를 입력하세요. :"))
print(5 + num)