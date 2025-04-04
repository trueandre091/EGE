with open("9_4589.txt") as f:
    data = [list(map(int, i.split())) for i in f]

from itertools import permutations

def f1(row):
    if max(row) < (sum(row) - max(row)):
        return True
    return False

def f2(row):
    u1 = row[0] + row[1]
    u2 = row[0] + row[2]
    u3 = row[0] + row[3]
    if any((sum(row) - i) == i for i in [u1, u2, u3]):
        return True
    return False

def f3(row):
    if any(
            (row[i[0]] + row[i[1]]) == (row[i[2]] + row[i[3]]) for i in permutations(range(4))
    ):
        return True
    return False


c = 0
for row in data:
    if f1(row) and f3(row):
        c += 1

print(c)


