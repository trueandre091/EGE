from itertools import *
from string import digits

alph = digits[:8]
nech = alph[1::2]

c = 0
for i in product(alph, repeat=5):
    if i[0] == "0":
        continue
    if i[0] not in nech:
        if i[-1] not in "26":
            if i.count("7") <= 2:
                c += 1

print(c)
