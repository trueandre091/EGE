from itertools import *

alph = "ДГИАШЭ"

c = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in "ИАЭ":
        if i[-1] not in "ДГШ":
            c += 1

print(c)
