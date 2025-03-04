from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

def f(n):
    res = ""
    while n:
        res = alph[n % 12] + res
        n //= 12
    return res

ch = alph[::2]
nech = alph[1::2]

c = []
for i in product(alph[:12], repeat=7):
    if i[0] == "0":
        continue
    i = "".join(i)

    if i.count("b") == 2:
        for j in range(7):
            if j % 2 == 0:
                if i[j] not in ch:
                    break
            else:
                if i[j] not in nech:
                    break
        else:
            c.append(i)
            continue

        for j in range(7):
            if j % 2 != 0:
                if i[j] not in ch:
                    break
            else:
                if i[j] not in nech:
                    break
        else:
            c.append(i)
            continue

print(c[-10:], len(c))


