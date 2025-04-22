from itertools import *

def check(word):
    c = 0
    for j in range(len(word) - 1):
        if word[j:j+2] in ("АА", "АИ", "ИА"):
            c += 1
    return c == 1


a = set()
for i in set(permutations("ПАРИЖАНКА")):
    i = "".join(i)
    if check(i):
        a.add(i)

print(len(a))





