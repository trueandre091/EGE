with open("24_4602.txt") as f:
    data = f.readline()

from re import *

pattern = r"([BCD][AO])+"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)) / 2)



