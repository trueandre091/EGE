def f(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: res |= {i, n // i}
    return sorted(res)

c = 0
for n in range(700001, 10**20):
    k = f(n)
    h = [i for i in k if i != n and i != 7 and str(i)[-1] == "7"]
    if any(h):
        print(n, min(h))
        c += 1
    if c == 5:
        break