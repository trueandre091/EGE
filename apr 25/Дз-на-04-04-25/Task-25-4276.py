def d(n):
    res = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(400_000_001, 10**20):
    k = sorted(list(d(n)), reverse=True)
    if len(k) >= 7:
        D = k[6]
        print(D, len(k))
        c += 1
    if c == 5:
        break

