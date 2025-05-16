from string import *
data = open("24_9791.txt").readline()

for c in ascii_uppercase[6:]:
    data = data.replace(c, " ")

data = data.split()
ans = 0

for i in data:
    s = i.lstrip("0")
    if int(s, 16) % 20 == 0:
        ans = max(ans, len(s))
    else:
        for st in range(len(s)):
            for en in range(st + 1, len(s) + 1)[::-1]:
                ss = s[st:en]
                if int(ss, 16) % 20 == 0:
                    ans = max(ans, len(ss))
                    break

print(ans)
