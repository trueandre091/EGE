from itertools import product
from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

RES = 0
for i in product(alph[:15], repeat=5):
    if i[0] == "0":
        continue

    i = "".join(i)
    c = 0
    for j in range(10, 15):
        if c >= 2:
            break
        c += i.count(alph[j])

    if c >= 2 and i.count("8") == 1:
        RES += 1
print(RES)