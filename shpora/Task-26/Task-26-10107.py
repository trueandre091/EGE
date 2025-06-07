with open("26_10107.txt") as f:
    N = int(f.readline())
    data = [list(map(int, l.split())) for l in f]

data = sorted(data, key=lambda x: (x[1], -x[0]))
ans = [data[0]]
for event in data.copy():
    if event[0] >= ans[-1][1]:
        ans.append(event)

ans.pop()
print(len(ans) + 1, max(data)[0] - ans[-1][1])




