# 사전 (dictionary)
# key-value pair (키-값 쌍)

# 사전 정의
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

# 타입을 출력해보자
print(type(my_dictionary))

# 사전의 키값을 이용하여 값을 출력해보자
print(my_dictionary[3])

# 사전에 한쌍의 키 값을 입력해보자
my_dictionary[9] = 81

# 결과를 출력해보자
print(my_dictionary)

# 키 값은 꼭 정수여야만하는가?      -> 아니다!

my_family = {
    '엄마': '송남숙',
    '아빠': '김종기',
    '오빠': '김동환',
    '본인': '김민정'
}

print(my_family)

# 사전의 키를 이용해 값을 찾아와 보자
print(my_family['본인'])