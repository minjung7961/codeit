# string_formatting 에서 배운 문자열포메팅
print("저는 {}, {}, {}를 좋아합니다!".format("의교", "엄마", "아빠"))
# 값 들어가는 순서를 바꾸고 싶다면 어떻게 할까?
print("저는 {1}, {0}, {2}를 좋아합니다!".format("의교", "엄마", "아빠"))
# {}안에 순서를 0부터 넣어준다

# 문자열에 숫자가 들어가는 포메팅
num_1 = 86
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))

# {2} 출력을 소숫점 아래 2자리만 출력하고싶으면 어떻게 할까?
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))

# 포메팅 종류는 총 3가지 1. % 2. format 메소드 3. f_string

# 기호 % 실습
s1 = "의교"
s2 = "엄마"
s3 = "아빠"
print("저는 %s, %s, %s를 좋아합니다" % (s1, s2, s3))

# format 메소드 실습하기
print("저는 {}, {}, {}를 좋아합니다".format(s1, s2, s3))

# f_string 실습하기
print(f"저는 {s1}, {s2}, {s2}를 좋아합니다")

favorit_string = f"저는 {s1}, {s2}, {s3}를 좋아합니다"
print(favorit_string)