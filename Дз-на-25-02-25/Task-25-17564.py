def f(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res |= {i, n // i}
    return sorted(res)

c = 0
for n in range(700001, 10**20):
    if c == 5:
        break
    d = f(n)
    if d:
        M = min(d) + max(d)
    else:
        M = 0

    if str(M)[-1] == "4":
        print(n, M)
        c += 1

