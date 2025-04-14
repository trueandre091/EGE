from itertools import *

s = set()

for i in product("01234", repeat=6):
    if i[0] == "0": continue
    i = "".join(i)
    if (i[0] == "3") and (int(i, 5) % 2 == 0): s.add(i)

print(len(s))



