from itertools import permutations

alph = "КИДАЛА"

c = set()
for i in permutations(alph, r=5):
    i = "".join(i)
    if "АА" not in i:
        c.add(i)

print(len(c))
