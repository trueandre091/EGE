with open("24_17563.txt") as f:
    data = f.readline()

from re import *

num = r"([7-9][0-9]*)"
pattern = rf"{num}([*-]{num})+"

data = [i.group() for i in finditer(pattern, data)]

print(max(data, key=len))
print(len(max(data, key=len)))




