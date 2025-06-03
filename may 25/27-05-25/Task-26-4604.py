with open("26_4604.txt") as f:
    f.readline()
    data = [int(i) for i in f]

data = sorted(data, reverse=True)

ans = [data[0]]

for box in data:
    if box + 3 <= ans[-1]:
        ans.append(box)

print(len(ans), ans[-1])





