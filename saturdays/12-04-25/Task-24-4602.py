from re import *

with open("24_4602.txt") as f:
    data = f.readline().strip()


pattern = r"[BCD]([AO][BCD])+[AO]"

matches = finditer(pattern, data)
matches = [i.group() for i in matches]
print(len(max(matches, key=len)) / 2)


