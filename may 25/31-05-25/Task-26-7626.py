with open("26_7626.txt") as f:
    K = int(f.readline())
    N = int(f.readline())
    data = [tuple(map(int, i.split())) for i in f]

data = sorted(data)
c = 0
camera = [0] * K
last_ceil = 0

for bag in data:
    for i in range(K):
        if bag[0] > camera[i]:
            camera[i] = bag[1]
            c += 1
            last_ceil = i + 1
            break

print(c, last_ceil)




