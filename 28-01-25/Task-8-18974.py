from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

ch = alph[::2]
nech = alph[1::2]

c = 0
for i in product(alph[:25], repeat=4):
    if i[0] == "0":
        continue

    nech_c = [k for k in i if int(k, 36) % 2 != 0]
    c5 = [k for k in i if int(k, 36) <= 5]
    if len(nech_c) == 1 and len(c5) <= 2:
        c += 1

print(c)










