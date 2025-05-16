with open("24_4643.txt") as f:
    data = f.readline().strip()

from re import *

pattern = r"([12]{2}[AB])+"

data = [i.group() for i in finditer(pattern, data)]

print(len(max(data, key=len)) / 3)

