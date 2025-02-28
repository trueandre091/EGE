def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n //i}
    return res

a = []
c = 0
for n in range(400_000_001, 10**20):
    k = sorted(f(n))
    if len(k) >= 7:
        print(k[-7], len(k))
        c += 1
    if c == 5:
        break



