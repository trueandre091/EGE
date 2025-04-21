from itertools import *
from string import digits

c = 0
for i in product(digits[:9], repeat=7):
    if i[0] == "0":
        continue

    i = "".join(i)
    if i[-1] not in "347":
        if not any(j * 3 in i for j in digits[:9]):
            c += 1

print(c)
