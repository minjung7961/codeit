# 리스트 를 배워봅시다

# 리스트 정의
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# 리스트 전체 출력
print(numbers)
print(names)

# 리스트의 요소를 하나씩 가져오기 - 인덱싱
print(numbers[1] + numbers[3])

# 다른방법으로 가져오기(음수사용)
print(numbers[5])
print(numbers[-1])

# 리스트 슬라이싱
print(numbers[0:4])
print(numbers[2:])
print(numbers[:3])

# 새로운 리스트 생성 _ 리스트 슬라이싱을 이용함
new_list = numbers[:3] # [2, 3, 5]
print(new_list[2])

# 리스트의 요소 변경
numbers[0] = 7
print(numbers)

numbers[0] = numbers[0] + numbers[1]
print(numbers)