def f(n):
    if n == 1 or n == 0:
        return True
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(1273547, 10**20):
    d = f(n)
    if d:
        M = sum(d)
    else:
        M = 0

    ost = M % (10**5)
    if not f(ost):
        print(n, M)
        c +=1
    if c == 5:
        break

# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609

