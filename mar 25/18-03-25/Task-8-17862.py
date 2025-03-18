from itertools import product
from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

c = []
for i in product(alph[:12], repeat=5):
    if i[0] == "0":
        continue
    ch8 = [j for j in i if int(j, 36) > 8]
    if i.count("7") == 1 and len(ch8) <= 3:
        c.append(i)
        print("".join(i))

print(len(c))

