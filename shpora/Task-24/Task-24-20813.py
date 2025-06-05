with open("24_20813.txt") as f:
    origin = f.readline().strip()

from re import *

num = r"([789][0789]*|0)"
pat = rf"{num}([-*]{num})*"

data = [i.group() for i in finditer(pat, origin)]
print(len(max(data, key=len)))



