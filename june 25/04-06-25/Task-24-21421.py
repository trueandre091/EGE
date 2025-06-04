from re import *

with open("24_21421.txt") as f:
    data = f.readline().strip()

from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:12]
ch = alph[::2]

pattern = rf"[{alph[1:]}][{alph}]*[{ch}]"

data = [i.group() for i in finditer(pattern, data)]
ans = []
for s in data:
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            sub_s = s[i:j].lstrip("0")
            if sub_s[-1] in ch:
                ans.append(sub_s)
                break
        else:
            continue
        break

print(len(max(ans, key=len)))




