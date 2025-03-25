with open("26_2717.txt") as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

from itertools import groupby

data = sorted(data)

ans = []
for row, seats in groupby(data, key=lambda x: x[0]):
    seats = [i[1] for i in seats]
    if len(seats) >= 5:
        c = 1
        for i in range(len(seats) - 4):
            seats5 = seats[i:i + 5]
            for j in range(4):
                if abs(seats5[j + 1] - seats5[j]) > 3:
                    break
            else:
                ans.append((row, seats5))
                break

print(ans)
