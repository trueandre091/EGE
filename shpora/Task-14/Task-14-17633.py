n = 6**260 + 6**160 + 6**60
for x in range(1, 2030):
    num = n - x
    c0 = 0
    while num:
        if num % 6 == 0: c0 += 1
        num //= 6
    if c0 == 202:
        print(x)