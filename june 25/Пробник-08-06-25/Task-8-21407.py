from itertools import *

alph = set("ДГИАШЭ")

c = 0
for i in product(alph, repeat=5):
    if i[0] not in "ИАЭ":
        if i[-1] not in "ДГШ":
            c += 1

print(c)
