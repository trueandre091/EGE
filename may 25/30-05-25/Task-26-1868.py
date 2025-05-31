with open("26_1868.txt") as f:
    f.readline()
    data = [list(map(int, i.split())) for i in f]

# data = [
#     (50, 12),
#     (50, 15),
#     (60, 157),
#     (60, 160),
#     (60, 22),
#     (60, 25)
# ]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for seat1, seat2 in zip(data, data[1:]):
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] - 1 == 2:
            print(seat1[0], seat1[1] + 1)
            break




