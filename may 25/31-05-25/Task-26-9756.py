with open("26_9756.txt") as f:
    N = int(f.readline())
    data = [tuple(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (x[1], -x[0]))
ans = [data[0]]

for event in data:
    if ans[-1][1] <= event[0]:
        ans.append(event)

ans.pop()

m = 0
for event in data:
    if ans[-1][1] <= event[0]:
        m = max(m, event[1])

print(m)

