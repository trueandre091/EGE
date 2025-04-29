def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for n in range(10**9 + 1, 10**20):
    if str(n) == str(n)[::-1]:
        d = f(n)
        if d:
            maxx = max(d)
            if maxx % 7 == 0:
                c += 1
                print(n, maxx)
    if c == 5:
        break



