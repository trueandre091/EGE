from re import *

with open("24_18284.txt") as f:
    data = f.readline()


pattern = r"L[^L]*?O.*?V.*?E"

matches = finditer(pattern, data)
matches = [i.group() for i in matches]

print(len(min(matches, key=len)))


