from random import randint


def generate_numbers(length):
    result_list = [randint(1, 45)]
    i = 1
    while i in range(1, length):
        num = randint(1, 45)
        if num in result_list:
            continue
        result_list.append(num)
        i += 1
    return result_list


def draw_winning_numbers():
    return generate_numbers(7)


def count_matching_numbers(sysnum, usernum):
    count_matching = 0
    bonus = 0
    for i in range(len(sysnum)):
        if sysnum[i] in usernum:
            count_matching += 1
    if count_matching == 5:
        bonus = 1
    return count_matching, bonus


def check(sysnum, usernum):
    count_match, bonus = count_matching_numbers(sysnum[:-1], usernum)
    if count_match == 6:
        print(1000000000)
    elif count_match == 5:
        num = 1000000
        if bonus == 1:
            num = 50000000
        print(num)
    elif count_match == 4:
        print(50000)
    elif count_match == 3:
        print(5000)
    else:
        print(0)


for i in range(1000):
    list_2 = generate_numbers(6)
    list_1 = draw_winning_numbers()
    count_matching_numbers(list_1, list_2)
    check(list_1, list_2)