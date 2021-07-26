import random as r


def input_user_numbers():
    u_number = []
    i = 0
    while i < 3:
        num = int(input(f'{i + 1}번째 숫자를 입력하세요: '))
        if num > 9:
            print('범위를 벗어나는 숫자 입니다. 다시 입력하세요.')
            continue
        elif num in u_number:
            print('중복되는 숫자 입니다. 다시 입력하세요.')
            continue
        u_number.append(num)
        i += 1
    return u_number


def create_ran_nums():
    c_number = []
    i = 0
    while i < 3:
        num = r.randint(0, 9)
        if num in c_number:
            continue
        c_number.append(num)
        i += 1
    return c_number


def checking_the_result(u_list, s_list):
    b = 0
    s = 0
    for i in range(3):
        """
        if u_list[i] in s_list:
            if u_list[i] == s_list[i]:
                s += 1
            else:
                b += 1
        """
        if u_list[i] == s_list[i]:
            s += 1
        elif u_list[i] in s_list:
            b += 1

    if s == 3:
        return '3S'
    elif b == 3:
        return  '3B'
    else:
        return str(s) + "S " + str(b) + "B"


u_list = []
s_list = create_ran_nums()
result = ""
count = 0

print(s_list)
print('0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.')
while result != '3S':
    print()
    print('숫자 3개를 하나씩 차례대로 입력하세요.')
    u_list = input_user_numbers()
    count += 1
    print(u_list)
    result = checking_the_result(u_list, s_list)
    print(result)

print(f"축하합니다 {count}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")
