n = 4**163 * 5 + 12**62

for x in range(1, 2006):
    num = n - x
    c1, c4 = 0, 0
    while num:
        if num % 5 == 1:
            c1 += 1
        elif num % 5 == 4:
            c4 += 1
        num //= 5
    if c1 < c4:
        print(x)

