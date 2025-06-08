from re import *
from string import digits, ascii_uppercase

with open("24_21908.txt") as f:
    data = f.readline().strip()

alph = (digits + ascii_uppercase)[:14]
ch = alph[::2]
pattern = rf"[{alph[1:]}][{alph}]*"

data = [i.group() for i in finditer(pattern, data)]
ans = []
for s in data:
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            subs = s[i:j].lstrip("0")
            if subs and subs[-1] in ch:
                ans.append(subs)
                break

print(len(max(ans, key=len)))



