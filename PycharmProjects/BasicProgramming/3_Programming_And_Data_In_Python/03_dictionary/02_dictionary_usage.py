my_family = {
    '엄마': '송남숙',
    '아빠': '김종기',
    '오빠': '김동환',
    '본인': '김민정'
}

# 값만 출력하기
print(my_family.values())

# 김민정이 있는지 확인하는 방법
print('김민정' in my_family.values())

# 반복문으로 값 출력하기

for value in my_family.values():
    print(value)


# 키 값 출력하기
print(my_family.keys())

# 키 값 반복문으로 출력하기
for key in my_family.keys():
    print(key)

# 응용!! 키 값으로 반복문을 이용해 출력하기!

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

# 더 간단하게 하는방법은?

for key, value in my_family.items():
    print(key, value)