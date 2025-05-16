with open("24_12254.txt") as f:
    data = f.readline().strip()

from re import *

st, en = r"(SQ|Q)?", r"(RS|R)?"
pattern = rf"{st}(RSQ)+{en}"

data = [i.group() for i in finditer(pattern, data)]

print(len(max(data, key=len)))