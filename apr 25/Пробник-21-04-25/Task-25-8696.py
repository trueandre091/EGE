def f(n):
    if n < 2:
        return set()
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for N in range(1_273_548, 10**20):
    d = f(N)
    if d:
        M = sum(d)
        if not f(M % 100_000):
            print(N, M)
            c += 1
        if c == 5:
            break
    else:
        M = 0

