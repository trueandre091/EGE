def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n //i}
    return res

for n in range(112_500_000, 112_550_001):
    k = f(n)
    if len(k) >= 2:
        M = sum(sorted(k)[-2:])
    else:
        M = 0
    if str(M)[-4:] == "1214":
        print(n)

