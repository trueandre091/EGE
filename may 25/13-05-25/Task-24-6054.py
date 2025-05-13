with open("24_6054.txt") as f:
    data = f.readline()

from re import *

pattern = r"([BC][BC]A)+"

data = [i.group() for i in finditer(pattern, data)]
print(len(max(data, key=len)))


