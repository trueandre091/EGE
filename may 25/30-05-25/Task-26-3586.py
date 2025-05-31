with open("26_3586.txt") as f:
    f.readline()
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))
ans = []
for tree1, tree2 in zip(data, data[1:]):
    if tree1[0] == tree2[0]:
        if tree2[1] - tree1[1] - 1 >= 1:
            ans.append((tree1[0], tree2[1] - tree1[1] - 1))

ans = sorted(ans, key=lambda x: (-x[1], -x[0]))

print(*ans[0])


