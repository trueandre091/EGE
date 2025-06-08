with open("24_21421.txt") as f:
    data = f.readline().strip()

from string import digits, ascii_uppercase
from re import *

alph = digits + ascii_uppercase
alph = alph[:12]

pat = rf"[{alph[1:]}][{alph}]*"

mat = [i.group() for i in finditer(pat, data)]
ans = []

for s in mat:
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            sub_s = s[i:j]
            if sub_s[-1] in alph[::2]:
                ans.append(sub_s)
                break
        else:
            continue
        break

print(len(max(ans, key=len)))


