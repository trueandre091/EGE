def dels(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res |= {i, n // i}
    return sorted(res)

c = 0
for i in range(500001, 10**10):
    if c == 5:
        break
    l = dels(i)
    h = [j for j in l if j != 8 and j != i and str(j)[-1] == "8"]
    if any(h):
        print(i, min(h))
        c += 1