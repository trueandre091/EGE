from string import digits, ascii_lowercase
from itertools import product

alph = digits + ascii_lowercase

c = 0
for i in product(alph[:12], repeat=5):
    if i[0] == "0":
        continue

    i = "".join(i)
    if i.count("7") == 1:
        if len([1 for k in i if int(k, 36) > 8]) <= 3:
            c += 1

print(c)