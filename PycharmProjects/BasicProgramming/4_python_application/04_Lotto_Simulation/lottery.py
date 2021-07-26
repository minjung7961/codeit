from random import randint


def generate_numbers(n):
    MAX_NUM = 45
    MIN_NUM = 1
    g_list = []
    for i in range(n):
        g_list.append(randint(MIN_NUM, MAX_NUM))

    return g_list


def generate_numbers(n):
    MAX_NUM = 45
    MIN_NUM = 1
    g_list = []
    for i in range(n):
        g_list.append(randint(MIN_NUM, MAX_NUM))

    return g_list


def draw_winning_numbers():
    d_w_list = generate_numbers(7)
    return sorted(d_w_list[:6]) + d_w_list[6:]


def count_matching_numbers(list_1, list_2):
    count = 0
    for num in list_1:
        if num in list_2:
            count += 1

    return count


def check(numbers, winning_numbers):
    n_count = count_matching_numbers(numbers, winning_numbers[:6])
    b_count = count_matching_numbers(numbers, winning_numbers[6:])
    if n_count == 6:
        return 1000000000
    elif n_count == 5:
        if b_count == 1:
            return 50000000
        else:
            return 1000000
    elif n_count == 4:
        return 50000
    elif n_count == 3:
        return 5000
    else:
        return 0


