def f(n):
    res = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(1, 10**20):
    N = 750_000 + n
    k = f(N)
    ch = [i for i in k if i % 2 == 0]
    if len(ch) % 2 != 0:
        print(n, len(ch))
        c += 1
    if c == 5:
        break
