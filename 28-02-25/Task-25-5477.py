def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(600001, 10**20):
    if n % 6 == 0:
        if not f(n - 1) and not f(n + 1):
            print(n-1, n+1)
            c += 1
    if c == 6:
        break

