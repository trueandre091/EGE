with open("26_4205.txt") as f:
    N = int(f.readline())
    data = [tuple(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for p in zip(data, data[1:]):
    tree1, tree2 = p
    if tree2[0] == tree1[0]:
        if tree2[1] - tree1[1] - 1 == 13:
            print((tree1[0], tree1[1] + 1))
            break





