with open("24_9845.txt") as f:
    data = f.readline()

from re import *

for i in "ABC":
    data = data.replace(i, "G")

for i in "89":
    data = data.replace(i, "A")

while "GG" in data:
    data = data.replace("GG", "G G")
while "AA" in data:
    data = data.replace("AA", "A A")

data = data.split()

print(len(max(data, key=len)))


