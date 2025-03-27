from itertools import product

alph = sorted(set("ЛУНАТИК"))

for pos, i in enumerate(product(alph, repeat=6), 1):
    i = "".join(i)
    if ((i.count("У") + i.count("А") + i.count("И")) == 1) and (i[0] == "Н"):
        print(pos, i)




