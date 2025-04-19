from re import *

with open("24_21597.txt") as f:
    data = f.readline()

num = r"([1-5][0-5]*|0)"
pattern = rf"{num}(\*{num})+(\-{num})+"
pattern = rf"(?=({pattern}))"

matches = finditer(pattern, data)
matches = [i.group(1) for i in matches]
print(len(max(matches, key=len)))



