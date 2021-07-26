# 쓰고있는 데이터갑의 타입이 궁금할떄는?  -> type 함수를 쓰자
#   숫자형의 데이터값 확인예시
print(type(3))  # int
print(type(3.0))  # float
print(type("3"))  # str
#   boolean 형의 데이터값 확인 예시
print(type(True))  # boolean
print(type("True"))  # string


#   기타 데이터값 출력 예시
def hello():
    print("Hello world")


print(type(hello))  # function
print(type(print))  # builtin_function_or_method - 내장되어있는 함수 이거나 또는 메소드
