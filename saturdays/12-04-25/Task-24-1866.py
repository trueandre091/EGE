with open("24_1866.txt") as f:
    data = f.readline().strip()

from re import *


pattern = r"(?<=ad|da)\w+?(?=ad|da)"

matches = findall(pattern, data)

print(len(max(matches, key=len)) + 2)






