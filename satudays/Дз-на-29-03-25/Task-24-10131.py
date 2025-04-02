with open("24_10131.txt") as f:
    data = f.readline()

from re import *
from string import ascii_uppercase

for i in ascii_uppercase[2:]:
    data = data.replace(i, "0")

print(data)




