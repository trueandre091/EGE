def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n // i}
    return res

c = 0
for N in range(10**7 + 1, 10**20):
    d = f(N)
    if len(d) >= 3:
        d = sorted(list(d))
        S = sum(d[-3:])
        if S**0.5 % 1 == 0:
            print(S)
            c += 1
    if c == 5:
        break

# 6007401
# 8940100
# 2582449
# 8300161
# 2105401