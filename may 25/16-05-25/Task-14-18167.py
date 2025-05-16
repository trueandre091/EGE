num = 6**900 + 6**10

for x in range(1, 10000):
    n = num - x
    c3, c5 = 0, 0
    while n:
        if n % 6 == 3: c3 += 1
        if n % 6 == 5: c5 += 1
        n //= 6
    if c3 == c5:
        print(x)



