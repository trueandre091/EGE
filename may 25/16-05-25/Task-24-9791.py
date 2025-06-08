from string import *
data = open("24_9791.txt").readline()

for c in ascii_uppercase[6:]:
    data = data.replace(c, " ")

data = data.split()
ans = 0

for i in data:
    s = i.lstrip("0")
    ans = max(len(s), ans)

print(ans)
