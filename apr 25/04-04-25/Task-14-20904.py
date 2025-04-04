
for x in range(1, 2031):
    num = 3**100 - x
    c = 0
    while num:
        if num % 3 == 0:
            c += 1
        num //= 3
        if c > 1:
            break
    else:
        print(x)





