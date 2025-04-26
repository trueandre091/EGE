with open("24-8100.txt") as f:
    data = f.readline()

from re import *

num1 = r"(([1-9][0-9]*[12346789])|[12346789])"
num2 = r"(([1-9][0-9]*[05])|[05])"
pattern = rf"(\({num1}[+-]{num2}\))+"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))



