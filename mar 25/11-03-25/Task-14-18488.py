n = 7**666 + 7**333 - 343


for x in range(1, 1000):
    num = n + 49**x
    k = 0
    while num:
        if num % 7 == 6:
            k += 1
        num //= 7
    if k == 49:
        print(x)
        break