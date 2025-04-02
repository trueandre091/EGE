with open("24_5237.txt") as f:
    data = f.readline()

from re import *

pattern = r"(X(YX)*)|(Y(XY)*)"

matches = finditer(pattern, data)

ans = [i.group() for i in matches]

print(len(max(ans, key=len)))

