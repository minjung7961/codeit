"""
    10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.

while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
"""

"""
i = 2
i_sum = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        i_sum += i
    i += 1

print(i_sum)

"""

i = 1000
i_sum = 0
while i > 0:
    if i % 2 == 0 or i % 3 == 0:
        i_sum += i
    i -= 1

print(i_sum)