from itertools import *

alph = sorted(set("ИНСТАВК"))

pos = 0

for i in product(alph, repeat=4):
    i = "".join(i)
    if i[0] in "НСТВК" and i[-1] in "ИА":
        pos += 1
        if i == "НИКА":
            print(pos, i)


