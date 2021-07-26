a_min = 1
b_min = 2
c_min = 3

c_max = 10

c = c_min
a = a_min
b = b_min


while b > a > 0:
    while c > b > a:
        while c < c_max & b < c:
            print(f"a {a} b {b} c {c}")
            c += 1
        c = c_min
        b += 1
    b = b_min
    a += 1


# 이게 안돌아가 는 이유 ? -> 0<a<b<c 가 한번이라도 아니면 멈추기 때문이다.



