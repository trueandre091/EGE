with open("26_16390.txt") as f:
    S, N = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
ans = []
for a in data.copy():
    if a <= S:
        ans.append(a)
        S -= a
        data.remove(a)
S += ans.pop()
data = sorted(data, reverse=True)
for a in data:
    if a <= S:
        ans.append(a)
        S -= a

print(len(ans), ans[-1])


