from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
print(alph[10:16])

gl = "ae"
c = 0
for i in product(alph[10:16], repeat=6):
    i = "".join(i)
    if i[0] not in gl and i[-1] not in gl:
        c += 1

print(c)
