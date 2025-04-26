with open("24-8058.txt") as f:
    data = f.readline()

from re import *

pattern = r"[A-C][a-c]*( [A-C]?[a-c]+)+\."

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))

