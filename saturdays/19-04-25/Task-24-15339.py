from re import *

with open("24_15339.txt") as f:
    data = f.readline()

pattern = r"([6-9]([A-C][6-9])+[A-C]?)|([A-C]([6-9][A-C])+[6-9]?)"

matches = finditer(pattern, data)
matches = [i.group() for i in matches]
print(len(max(matches, key=len)))

