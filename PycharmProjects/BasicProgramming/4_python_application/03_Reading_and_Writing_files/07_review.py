import random as rd
with open('r_vocabulary.txt', 'r', encoding='UTF-8') as f:
    lists = []
    for line in f:
        lists.append((line.strip()).split())

while True:
    num = rd.randint(0, len(lists)-1)
    ans = input(lists[num][0])
    if ans == 'q':
        break
    if ans == lists[num][1]:
        print('맞았습니다!')
    else:
        print(f'아쉽습니다. 정답은 {lists[num][1]}입니다.')
