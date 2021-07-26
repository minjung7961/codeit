# 1. spit 이란? -> 문자열을 특정 문자를 기준으로 잘라내어 리스트로 반환하는 모듈
my_string = "1. 2. 3. 4. 5. 6. "
print(my_string.split("."))

# 걸과보면 공백문자가 매우 아쉬움 그래서 없애는 방법을 고민해보자
#   1. strip 을 쓰자 - > 안됨
"""
my_strip_string = my_string.split(".")
print(my_strip_string.strip())
"""

#   2. split 의 기준을 "." 에서 ". "으로 바꾸자
print(my_string.split(". "))

# 2. 다른예시
full_name = "kim, yuna"
print(full_name.split(", "))
last_name = full_name.split(", ")[0]
first_name = full_name.split(", ")[1]
print(last_name)
print(first_name)

#3. 화이트 스페이스를 기준으로 나누는 방법 -> split()의 인자값을 안넘겨주면 됨
print("    \n\n   2   \t   3   \n   5 7 11   \n\n".split())