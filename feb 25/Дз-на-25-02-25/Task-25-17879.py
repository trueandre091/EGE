def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return sorted(res)

c = 0
for n in range(800001, 10**20):
    k = f(n)
    if k:
        M = min(k) + max(k)
    else:
        M = 0
    
