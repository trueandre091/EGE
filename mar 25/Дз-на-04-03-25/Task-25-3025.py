def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(2 * 10**8 + 1, 10**20):
    nech_d = [i for i in f(n) if i % 2 != 0]
    d = sorted(nech_d, reverse=True)
    if len(d) < 6:
        continue
    D = d[5]
    if D > 0:
        print(n, D)
        c += 1
    if c == 5:
        break

# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443


