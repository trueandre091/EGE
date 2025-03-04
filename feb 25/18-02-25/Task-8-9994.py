from itertools import product

alph = sorted(set("ШКОЛА"))

for pos, i in enumerate(product(alph, repeat=5), 1):
    i = "".join(i)
    if i == "ШАЛАШ":
        print(pos)

# 2555

