# from area import circle, square # area 모듈의 circle, square 가져오겠다
# import area as ar   # area 모듈을 ar 이라는 이름으로 사용하겠다.
# from area import square as sq #square 함수를 sq 이름으로 이용하겠다.
# from area import *    # 모든 함수를 가져온다 근데 권장은 안함
"""
print(circle(2))
print(square(3))
"""

x = [1, 2, 3, 4, 5]
y = x
y[2] = 6

print(x)
print(y)
print(x==y)

z = list(x)
z[2] = 8
print(x)
print(y)
print(z)
print(x==z)
