from itertools import *

alph = "01234567"
ch = alph[::2]
nech = alph[1::2]

c = 0
for i in product(alph, repeat=6):
    if i[0] == "0":
        continue
    i = "".join(i)
    if len(set(i)) == len(i):
        if not any("".join(a) in i for a in product(ch, repeat=2)) \
                and not any("".join(a) in i for a in product(nech, repeat=2)):
            if int(i, 8) % 5 == 0:
                c += 1

print(c)
