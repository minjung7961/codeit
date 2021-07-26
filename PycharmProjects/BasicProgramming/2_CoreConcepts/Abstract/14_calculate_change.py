def calculate_change(payment, cost):
    fif_b = 0
    ten_b = 0
    f_b = 0
    o_b = 0

    fif_b = (payment-cost)//50000
    ten_b = ((payment-cost) % 50000)//10000
    f_b = ((payment-cost) % 10000)//5000
    o_b = ((payment-cost) % 5000)//1000

    print(fif_b)
    print(ten_b)
    print(f_b)
    print(o_b)


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)