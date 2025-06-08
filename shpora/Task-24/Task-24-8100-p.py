from re import *

with open("24_8100.txt") as f:
    data = f.readline().strip()

A = r"([1-9][0-9]*[12346789]|[12346789])"
B = r"([1-9][0-9]*[05]|[05])"
pattern = rf"(\({A}[-+]{B}\))+"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))





