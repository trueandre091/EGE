from itertools import permutations

alph = "МАКАКА"

c = set()
for i in permutations(alph):
    i = "".join(i)
    if "АА" not in i and "КК" not in i:
        c.add(i)

print(len(c))