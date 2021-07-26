import random as r
voca_list = []
i = 0
with open('vocabulary.txt', 'r',encoding='UTF-8') as f:
    for line in f:
        data = line.strip()
        voca_list.append(data.split(": "))
    while True:

        i = r.randint(0,6)
        mean = voca_list[i][1]
        voca = voca_list[i][0]
        answer = input(f'{mean}: ')
        if answer == 'q':
            break
        if answer == voca:
            print('맞았습니다!\n')
        else:
            print(f'틀렸습니다. 정답은 {voca}입니다')


