n = 43**56 + 113**841

for x in range(1, 2006):
    num = n - x
    ch, nech = 0, 0
    c2 = 0
    while num:
        if num % 4 == 2: c2 += 1
        if (num % 4) % 2 == 0: ch += 1
        else: nech += 1
        num //= 4
    if c2 <= 712:
        if ch % 2 == 0:
            if nech % 2 == 0:
                print(x)
