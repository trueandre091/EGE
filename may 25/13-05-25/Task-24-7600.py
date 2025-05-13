with open("24_7600.txt") as f:
    data = f.readline()

from itertools import *


for i in product("QRS", repeat=2):
    k = "".join(i)
    while k in data:
        data = data.replace(k, f"{i[0]} {i[1]}")

data = data.split()

print(len(max(data, key=len)))


