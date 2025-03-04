def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(220001, 10**20):
    d = f(n)
    if d: M = min(d) + max(d)
    else: M = 0
    if str(M)[-1] == "4":
        print(n, M)
        c += 1
    if c == 5: break

# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044