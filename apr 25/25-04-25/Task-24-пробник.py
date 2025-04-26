with open("24v1.txt") as f:
    data = f.readline()

from re import *


num = r"([0-9]+)"
pattern = rf"({num}=)+{num}"


matches = [i.group() for i in finditer(pattern, data)]

ans = []
for i in matches:
    i = i.strip("=")
    if ("=8=" in i) or i.startswith("8=") or i.endswith("=8"):
        ans.append(i)
    else:
        pos1 = i.find("8=")
        pos2 = i.rfind("=8")
        if pos1 != -1:
            ans.append(i[pos1:])
        if pos2 != -1:
            ans.append(i[:pos2 + 2])


print(len(max(ans, key=len)))
print(max(ans, key=len))

# гошанчик

# while "==" in data:
#     data = data.replace("==", " ")
#
# data = data.split()
#
# ans = []
# for i in data:
#     if ("=8=" in i) or (i[:2] == "8=") or (i[-2:] == "=8"):
#         ans.append(i)
#
# print(len(max(ans, key=len)))
# print(max(ans, key=len))


