from itertools import permutations

alph = "ХОЧУ В ВУЗ"

c = set()
for i in set(permutations(alph)):
    i = "".join(i)
    if i[0] == " " or i[-1] == " " or "  " in i:
        continue

    if all(not (k[0] == "У") for k in i.split()):
        c.add(i)

print(len(c) - 1)

# 75599
