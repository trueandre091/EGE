with open("24_6636.txt") as f:
    data = f.readline()

from re import *

pattern = r"([24][135])+"

data = [i.group() for i in finditer(pattern, data)]
print(len(max(data, key=len)) / 2)




