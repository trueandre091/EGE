with open("9_21408.txt") as f:
    data = [list(map(int, i.split())) for i in f]

# c = 0
# for row in data:
#     cs = [row.count(i) for i in row]
#     pov = [i for i in row if row.count(i) > 1]
#     nepov = [i for i in row if row.count(i) == 1]
#     if (cs.count(3) == 6) and (cs.count(1) == 1):
#         if max(pov) > nepov[-1]:
#             c += 1

def f1(row):
    cs = [row.count(i) for i in row]
    return cs.count(3) == 6 and cs.count(1) == 1

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1][-1]
    return max(pov) > nepov

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)

