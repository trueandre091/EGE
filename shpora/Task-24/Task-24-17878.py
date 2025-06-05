with open("24_17878.txt") as f:
    origin = f.readline().strip()

from re import *

num = r"([6789][06789]*|0)"
pat = rf"{num}([-*]{num})*"

data = [i.group() for i in finditer(pat, origin)]
print(len(max(data, key=len)))


