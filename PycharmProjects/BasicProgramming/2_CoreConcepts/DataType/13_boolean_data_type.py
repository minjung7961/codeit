# boolean 연산
print(True)     # true
print(False)    # true
# and 연산
print(True and True)    # true
print(True and False)   # false
print(False and True)   # false
print(False and False)  # false
# or 연산
print(True or True)     # true
print(False or True)    # true
print(True or False)    # true
print(False or False)   # false
# not 연산
print(not True)         # False
print(not False)        # true
# 숫자 연산 적용
print(2 > 1)            # true
print(2 < 1)            # false
print(3 >= 2)           # true
print(3 <= 2)           # false
print(2 == 2)           # True
print(2 != 2)           # false
# 문자열 연산 적용
print("Hello" == "Hello")   # true
print("Hello" != "Hello")   # false
# 응용하여 적용
print(2 > 1 and "Hello" == "Hello") # true
# 이중부정
print(not not True)     # true
print(not not False)    # false
# 3개 이상의 불린식
#   안햇갈리게 유의하기!!!
print(7 == 7 or (4 < 3 and 12 > 10))    # true or ( false and true ) -> true or false -> ture
# 변수를 사용하는 불린식
x = 3
print(x > 4 or not (x < 2 or x == 3))   # false or not ( false or true ) -> false or not ( ture ) -> fasle or false -> false