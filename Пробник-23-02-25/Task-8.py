from itertools import product

alph = sorted(set("КАЛЕЙДОСКОП"), reverse=True)

for pos, i in enumerate(product(alph, repeat=6), 0):
    i = "".join(i)
    if i[0] == "К" and i.count("Й") >= 2 and ("С" not in i) and ("Е" not in i):
        print(pos, i)

# 243698 КППОЙЙ




