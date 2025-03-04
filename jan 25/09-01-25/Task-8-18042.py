from itertools import product

alph = set("ЛЮСТРА")

sogl = "ЛСТР"
c = 0
for i in product(alph, repeat=5):
    if i.count("Ю") > 2:
        continue
    if i[-1] in sogl:
        continue
    c += 1

print(c)

# 2400
