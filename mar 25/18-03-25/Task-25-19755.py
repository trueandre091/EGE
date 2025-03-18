def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res


c = 0
for n in range(1200001, 10**20):
    d = f(n)
    if [i for i in d if not f(i)]:
        pr = [i for i in d if not f(i)]
        M = min(pr) + max(pr)
    else:
        M = 0
    if (M > 2000) and (str(M)[-1] == "8"):
        print(n, M)
        c += 1
    if c == 5:
        break
