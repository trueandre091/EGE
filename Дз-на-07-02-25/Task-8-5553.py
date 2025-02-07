from itertools import permutations

alph = "СОТОЧКА"

c = 0
for i in set(permutations(alph)):
    i = "".join(i)
    if "ОО" in i or "АО" in i or "ОА" in i:
        c += 1

print(c)

# 1800
