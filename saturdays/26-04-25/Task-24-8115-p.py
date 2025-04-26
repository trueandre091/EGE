with open("24-8115.txt") as f:
    data = f.readline()

from re import *
from string import *


alph = digits + ascii_uppercase
alph = alph[:14]

pattern = rf"1[{alph}]*"

matches = [i.group() for i in finditer(pattern, data)]

ans = []
for i in matches:
    for st in range(len(i) - 1):
        if i[st] != "1":
            continue
        for en in range(st + 1, len(i)):
            num = i[st:en + 1]
            if int(num, 14) % 7 == 0:
                ans.append(num)



print(len(max(ans, key=len)))



