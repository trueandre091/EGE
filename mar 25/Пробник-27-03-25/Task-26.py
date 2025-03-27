with open("26-input.txt") as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

# data = [
#     [20, 876],
#     [100, 350],
#     [131, 140],
#     [150, 310],
#     [120, 200]
# ]

from math import ceil

for i in range(len(data)):
    z = data[i]
    data[i] = [z[0], z[0] + ceil(z[1] / 10), z[1]]

data = sorted(data, key=lambda x: (x[1], x[0]))

ans = [data[0]]
for z in data[1:]:
    if z[0] >= ans[-1][1]:
        ans.append(z)

print(len(ans))
print(sum([i[2] for i in ans]))

# 12740
# 10598





