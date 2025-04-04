from itertools import product
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

c = 0
for i in product(alph[:7], repeat=5):
    if i[0] == "0":
        continue
    ch = [int(j) for j in i if int(j) % 2 == 0]
    nech = [int(j) for j in i if int(j) % 2 != 0]
    if i.count("6") == 1 and sum(ch) < sum(nech):
        c += 1

print(c)

