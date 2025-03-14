def d(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(200_000_001, 10**20):
    k = sorted(d(n), reverse=True)
    k = [i for i in k if i % 2 != 0]
    if len(k) < 6:
        continue
    else:
        print(n, k[5])
        c += 1
    if c == 5:
        break
