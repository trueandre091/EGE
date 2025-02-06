from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

n = [j * 3 for j in alph[:10]]
c = 0
for i in product(alph[:9], repeat=7):
    if i[0] in ["2", "4", "6", "0"]:
        continue

    i = "".join(i)
    if i[-3:] not in n:
        c += 1

print(c)



