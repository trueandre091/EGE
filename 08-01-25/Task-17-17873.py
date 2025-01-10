with open("17_input.txt") as f:
    data = list(int(l) for l in f)

m = min(data)
c = 0
maxx = -1
for i in range(len(data) - 1):
    a1 = data[i]
    a2 = data[i + 1]
    if a1 % 16 == m or a2 % 16 == m:
        c += 1
        maxx = max(maxx, a1 + a2)

print(c, maxx)

# 1214 176024