from re import *

with open("24_18597.txt") as f:
    data = f.readline()


pattern = r"[1-9][0-9]{3}\.[0-9]+&[1-9][0-9]{3}\.[0-9]+"

matches = finditer(pattern, data)
matches = [i.group() for i in matches]

print(len(max(matches, key=len)))

