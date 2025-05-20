with open("24_17641.txt") as f:
    data = f.readline()

from re import *
from string import *

num = r"([1-9][0-9]*|0)"
pattern = rf"{num}([+*]{num})+"

data = [i.group() for i in finditer(pattern, data)]
ans = []

for virazhenie in data:
    if eval(virazhenie) == 0:
        ans.append(len(virazhenie))
    else:
        for l in range(len(virazhenie) + 1):
            for r in range(len(virazhenie), l + 1, -1):
                n_virazhenie = virazhenie[l:r].strip("+*")
                if len(n_virazhenie) < 2:
                    break
                if n_virazhenie[0] == "0" and n_virazhenie[1] in digits:
                    continue
                if eval(n_virazhenie) == 0:
                    ans.append(len(n_virazhenie))
                    break

print(max(ans))
