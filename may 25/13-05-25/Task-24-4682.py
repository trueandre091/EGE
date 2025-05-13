with open("24_4682.txt") as f:
    data = f.readline()

from re import *

pattern = r"([AE][BCD])+"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)) / 2)


