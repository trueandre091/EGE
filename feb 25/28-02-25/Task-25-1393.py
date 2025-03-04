def f(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(650_001, 10**20):
    k = f(n)
    if k:
        pr = [i for i in k if not f(i)]
        F = sum(pr) // len(pr)
    else:
        F = 0
    if F % 37 == 23:
        print(n, F)
        c += 1
    if c == 4:
        break
