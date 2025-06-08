with open("24_17641.txt") as f:
    data = f.readline()

from re import *
from string import *

num = r"([1-9][0-9]*|0)"
pattern = rf"{num}([+*]{num})+"

data = [i.group() for i in finditer(pattern, data)]
ans = 0

for virazhenie in data:
    if eval(virazhenie) == 0:
        ans = max(ans, len(virazhenie))
    elif len(virazhenie) > ans:
        for l in range(len(virazhenie)):
            for r in range(len(virazhenie), l, -1):
                n_virazhenie = virazhenie[l:r].strip("+*")
                if len(n_virazhenie) < 2 or n_virazhenie[0] == "0" and n_virazhenie[1] in digits:
                    break
                if eval(n_virazhenie) == 0:
                    ans = max(ans, len(n_virazhenie))
                    break

print(ans)
# 142
