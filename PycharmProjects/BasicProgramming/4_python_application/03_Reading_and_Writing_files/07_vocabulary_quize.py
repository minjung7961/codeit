with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        str = line.strip()
        print(str.split())

        mean = input(str.split()[0] + " ")
        if mean == str.split()[1]:
            print('맞았습니다!\n')
        else:
            print(f'아쉽습니다. 정답은 {str.split()[1]}입니다.\n')