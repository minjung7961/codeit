with open('r_vocabulary.txt', 'a', encoding='UTF8') as f:
    while True:
        voc = input('영어 단어를 입력하세요: ')
        if voc == 'q':
            break
        f.write(voc+": ")
        mean = input('한국어 뜻을 입력하세요: ')
        if mean == 'q':
            break
        f.write(mean+"\n")
