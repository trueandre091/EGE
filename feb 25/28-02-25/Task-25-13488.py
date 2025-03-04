def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n //i}
    return res


for n in range(18782, 18823):
    k = f(n)
    nech = sorted([i for i in k if i % 2 != 0])
    if len(nech) == 3:
        print(*nech)

