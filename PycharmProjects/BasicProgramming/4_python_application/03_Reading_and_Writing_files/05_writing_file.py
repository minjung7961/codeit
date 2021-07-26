with open('new_text_file.txt', 'w', encoding='UTF-8') as f: # 'w' 이거 덮어쓸떄 쓰는거임
    f.write("hello\n")
    f.write("my name is minjung\n")


# 추가하여 쓰고 싶을때는 어케 할까? -> 'w' 를 'a'로 바꿔쓰자
with open('new_text_file.txt', 'a', encoding='UTF-8') as f:
    f.write("\n안녕\n")
    f.write("난 한국인이야!!")

# 'a' 는 appand의 줄임말이고 파일명이 없을떄는 그 파일을 새로 만들어 쓴다.