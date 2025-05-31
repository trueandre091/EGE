with open("26_3230.txt") as f:
    f.readline()
    data = [list(map(int, i.split())) for i in f]

# data = [
#     (40, 30),
#     (40, 34),
#     (50, 125),
#     (50, 129),
#     (50, 64),
#     (50, 68),
#     (50, 70)
# ]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for tree1, tree2 in zip(data, data[1:]):
    if tree1[0] == tree1[0]:
        if tree2[1] - tree1[1] - 1 == 11:
            print(tree1[0], tree1[1] + 1)
            break




