from re import *

with open("24_18147.txt") as f:
    data = f.readline()

pattern = r"[789]+(\+[789]+)+"
matches = finditer(pattern, data)

matches = [i.group() for i in matches]

print(max(eval(i) for i in matches))


