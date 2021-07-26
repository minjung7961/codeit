# 정렬 하기 위한 sort 함수와 sorted 함수를 배워보자
# 먼저 sorted 함수부터 배워보자

numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# 오름차순 정렬
new_list = sorted(numbers) # 정렬된 새로운 리스트를 리턴
print(new_list)

# 내림차순 정렬
new_list = sorted(numbers, reverse=True)
print(new_list)

# sorted 함수를 사용한 후의 numbers 의 리스트를 출력하면 어떻게 나올까?
print(numbers)

# 그대로 나온다 즉 기존 리스트는 건드리지 않음 정렬된 새로운 리스트를 리턴함

# sort() 함수를 써보자 어떻게 출력되는가?
print(numbers.sort())
# none 이 나온다
# 이유는 무엇인가?
#   - sort() 함수자체는 아무것도 리턴하지 않는다 대신에 numbers 리스트 자체를 정렬시킨다.
# 그렇다면 정렬된 리스트를 보려면 어떻게 해야하는가?
#   - print(numbers)
print(numbers)

# 내림차순으로 정렬하려면 어케해야하나?
numbers.sort(reverse=True)
print(numbers)