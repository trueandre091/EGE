with open("26-input.txt") as f:
    N = int(f.readline())
    data = {}
    for i in f:
        art, cost, st = i.split()
        art = int(art)
        cost = int(cost)
        st = int(st)
        if art in data:
            data[art][1] += 1
            data[art][2] += st
        else:
            data[art] = [cost, 1, st]

average = sum([i[0] for i in data.values()]) / len(data)
expensive = {key: value for key, value in data.items() if value[0] > average}
expensive = sorted(expensive.items(), key=lambda x: (-x[1][2], -x[1][0]))
print(expensive[0])