# 리스트의 함수에 대하여 알아보자

# 리스트 생성
numbers = []

# 리스트 길이 알려주는 함수
print(len(numbers))  # 0

# 리스트에 값 추가하는 함수
numbers.append(5)  # 가장 오른쪽에 추가됨
numbers.append(8)
print(numbers)
print(len(numbers))

# 리스트에 값 삭제하는 함수 del
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)
del numbers[3]
print(numbers)

# 리스트의 원하는 인덱스 위치에 삽입하기
numbers.insert(4, 37)
print(numbers)
