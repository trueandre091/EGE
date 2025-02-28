from itertools import product

alph = "КОТБУС"

c = 0
for i in product(alph, repeat=8):
    i = ''.join(i)
    if "КОТ" in i and i[0] not in "ОУ":
        c += 1

print(c)