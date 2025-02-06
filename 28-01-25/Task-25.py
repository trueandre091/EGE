from fnmatch import fnmatch


def div(n):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return res

k = 0
for n in range(65001, 10**6):
    if k == 7:
        break
    if not fnmatch(str(n), "6*97*5?"):
        continue

    divis = div(n)
    c = []
    for num in divis:
        if num % 2 == 0:
            c.append(num)

    if len(c) >= 4:
        print(n, sum(c))
        k += 1






















