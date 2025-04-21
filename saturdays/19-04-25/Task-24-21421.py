from re import *
from string import *

alph = digits + ascii_uppercase

with open("24_21421.txt") as f:
    data = f.readline()

pattern = rf"[{alph[1:12]}][{alph[:12]}]+[{alph[:12:2]}]"

matches = finditer(pattern, data)
matches = [i.group() for i in matches]

print(len(max(matches, key=len)))


