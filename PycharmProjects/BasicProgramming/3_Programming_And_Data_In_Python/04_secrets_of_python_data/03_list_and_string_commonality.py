# 리스트의 인덱싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

# 문자열의 인덱싱!!!!!!!!
alphabet_string = 'ABCDEFGHIJ'
print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

# 리스트 슬라이싱
print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

# 문자열 슬라이싱!!!!!!!!!!!!!
print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])

# 문자열 연결
str_1 = 'hello'
str_2 = 'world'
str_3 = str_1 + str_2
print(str_3)

# 리스트의 연결!!!!!!
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

# 리스트의 len()함수 출력
print(len(list_3))

# 문자열의 len()함수 출력
print(len(str_3))