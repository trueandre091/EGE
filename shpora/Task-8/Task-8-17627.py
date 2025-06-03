from itertools import *
from string import *

alph = digits + ascii_lowercase
alph = alph[:15]
c = 0
for i in product(alph, repeat=5):
    if i[0] == "0":
        continue
    if i.count("8") == 1:
        if sum(int(j, 36) > 9 for j in i) >= 2:
            c += 1

print(c)



