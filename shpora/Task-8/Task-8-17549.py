from itertools import *

alph = sorted(set("ФОКУС"))

for pos, i in enumerate(product(alph, repeat=5), 1):
    i = "".join(i)
    if "Ф" not in i and i.count("У") == 2:
        print(pos, i)

