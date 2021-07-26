# 상수 (constant)
PI = 3.14  # 원주율 '파이'
# 상수를 왜쓰는 것일까? 2가지이유가 있다 첫번째는 값을 고정하겠다는 의지 그리고 두번쨰는 실수를 줄이기 위해서이다


# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4  # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 5  # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6  # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))