import random


CHANCE = 4
NUM = random.randint(1, 20)

for i in range(CHANCE):
    user_num = int(input(f"기회가 {CHANCE}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "))
    if NUM > user_num:
        print("Up")
    elif NUM < user_num:
        print("Down")
    else:
        print(f"축하합니다. {i+1}번만에 숫자를 맞히셨습니다.")
        break

    if i == 3:
        print(f"아쉽습니다. 정답은 {NUM}였습니다.")