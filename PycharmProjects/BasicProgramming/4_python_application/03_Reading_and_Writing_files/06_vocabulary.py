voca = ''
mean = ''
with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
    while True:
        voca = input('영어 단어를 입력하세요: ')
        if voca == 'q':
            break
        f.write(voca + ': ')
        mean = input('한국어 뜻을 입력하세요: ')
        if mean == 'q':
            break
        f.write(mean + '\n')