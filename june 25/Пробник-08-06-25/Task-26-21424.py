with open("26_21424.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)
ans = [data[0]]
for box in data:
    if box + 9 <= ans[-1]:
        ans.append(box)

print(len(ans), ans[-1])


