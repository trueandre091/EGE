def f(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res |= {i, n // i}
    return sorted(res)

c = 0
for i in range(800001, 10**20):
    if c == 5:
        break
    K = f(i)
    if K: M = min(K) + max(K)
    else: M = 0

    if str(M)[-1] == "4":
        print(i, M)
        c += 1



