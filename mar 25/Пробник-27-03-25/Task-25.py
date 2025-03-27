def d(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res |= {i, n // i}
    return res

c = 0
for n in range(300_001, 10**20):
    k = d(n)
    if k:
        M = max(k) - min(k)
    else:
        M = 0
    if str(M)[-1] == "6":
        print(n, M)
        c += 1
    if c == 5:
        break



