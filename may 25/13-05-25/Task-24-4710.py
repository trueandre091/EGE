with open("24_4710.txt") as f:
    data = f.readline()

from re import *

pattern = r"([CDF][AO])+"

data = [i.group() for i in finditer(pattern, data)]

print(len(max(data, key=len)) / 2)


