with open("26_21424.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

# data = [
#     43, 40, 32, 40, 30
# ]

data.sort(reverse=True)
ans = [data[0]]
for box in data:
    if box + 9 <= ans[-1]:
        ans.append(box)

print(len(ans), min(ans))



