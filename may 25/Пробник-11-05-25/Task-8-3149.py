from itertools import *
from string import *

c = 0
for i in range(10**4, 10**5):
    i = str(i)
    if i[-1] not in "347":
        if not any((3 * j) in i for j in digits):
            c += 1

print(c)

# 606747


