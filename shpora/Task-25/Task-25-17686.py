def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(700_001, 10**20):
    d = f(n)
    d7 = [i for i in d if (str(i)[-1] == "7") and (i != 7)]
    if d7:
        print(n, min(d7))
        c += 1
    if c == 5:
        break