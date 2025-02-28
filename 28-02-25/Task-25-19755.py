def f(n):
    res = set()
    for i in range(2, int(n**.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(1200000, 10**20):
    k = f(n)
    if k:
        l = [i for i in k if not f(i)]
        M = min(l) + max(l)
    else:
        M = 0
    if M > 2000 and str(M)[-1] == "8":
        print(n, M)
        c += 1
    if c == 5:
        break
