with open("24_7624.txt") as f:
    data = f.readline()

from itertools import *

for i in product("XYZ", repeat=2):
    i = "".join(i)
    while i in data:
        data = data.replace(i, f"{i[0]} {i[1]}")

data = data.split()

print(len(max(data, key=len)))

