from itertools import product
from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

ch = alph[:16:2]

c = 0
for i in product(alph[:16], repeat=5):
    if i[0] == "0":
        continue

    i = "".join(i)

    f = True
    for k in ch:
        if k + "6" in i or "6" + k in i:
            f = False

    if i.count("6") == 2 and f:
        c += 1

print(c)
# 4352
