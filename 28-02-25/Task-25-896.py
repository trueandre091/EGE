def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n //i }
    return res

c = 1
for n in range(194441, 196501):
    if not f(n):
        if str(n)[-2:] == "93":
            print(c, n)
            c += 1
