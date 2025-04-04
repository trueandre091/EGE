from itertools import product

alph = sorted("АРГУМЕНТ")

for pos, i in enumerate(product(alph, repeat=4), 1):
    i = "".join(i)
    if len(set(i)) == len(i) and "".join(sorted(i)) == i:
        print(pos)





