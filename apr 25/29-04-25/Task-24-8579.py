with open("24_8579.txt") as f:
    data = f.readline()

from re import *

pat1 = r"((?<=[02468])[A-Z]+(?=[13579]))"
pat2 = r"((?<=[13579])[A-Z]+(?=[02468]))"
pattern = rf"{pat1}|{pat2}"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))






