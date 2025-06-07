with open("26_9847.txt") as f:
    N = int(f.readline())
    data = [tuple(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (x[0], x[1]))
timeline = [0] * 1441

for time in range(1441):
    gs = [g for g in data if g[0] <= time <= g[1]]
    timeline[time] = len(gs)

s = []
maxx = max(timeline)
c = 0
for time in range(len(timeline)):
    if timeline[time] == maxx:
        c += 1
    else:
        if c > 0:
            s.append((c, time - c, time - 1, maxx))
            c = 0

print(s)
