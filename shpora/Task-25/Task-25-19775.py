def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(32_500_001, 10**20):
    d = f(n)
    pr_d = [i for i in d if (not f(i)) and (i not in (0, 1))]
    if pr_d:
        S = sum(pr_d)
        if S and (S % 145 == 0):
            print(n, S)
            c += 1
    if c == 7:
        break
