def f(n):
    res = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res |= {i, n//i}
    return res
c = 0
for n in range(800001, 10**20):
    d = f(n)
    if len(d) <= 10:
        continue
    summ = sum(d)
    p = 1
    for i in d: p *= i

    if (p % 2 != 0) and (summ % 2 != 0):
        print(n, len(d))
        c += 1
    if c == 6:
        break
