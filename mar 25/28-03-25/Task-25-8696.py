def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(1_273_548, 10**20):
    d = f(n)
    if d:
        M = sum(d)
    else:
        M = 0
    if not f(M % 100_000) and M != 0:
        print(n, M)
        c += 1
    if c == 5:
        break
