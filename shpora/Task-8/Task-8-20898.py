from itertools import *
from string import *

alph = digits[:9]

c = 0
for i in product(alph, repeat=5):
    if i[0] == "0": continue
    i = ''.join(i)
    if i.count("0") == 1:
        if not any(("0" + j) in i or (j + "0") in i for j in alph[1::2]):
            c += 1

print(c)
