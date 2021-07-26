
"""
factor_count = 0
factor = 0
while factor <= 120:
    factor += 1
    if 120 % factor == 0:
        print(factor)
        factor_count += 1

print(f"120의 약수는 총 {factor_count}개입니다.")
"""

INTEGER_NUMBER = 120
i = 1
divisor_count = 0
while i <= INTEGER_NUMBER :
    if INTEGER_NUMBER % i == 0:
        print(i)
        divisor_count += 1
    i += 1
print(divisor_count)