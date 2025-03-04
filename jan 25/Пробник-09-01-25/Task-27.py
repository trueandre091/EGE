with open("27-B-input.txt") as f:
    data = [int(i) for i in f]

K = 1666626

maxx = -1
r = []
for l in range(K, len(data) + 1):
    for i in range(len(data) - l + 1):
        road = (data[i:i + l], l)
        summ = sum(road[0])
        if summ > maxx:
            maxx = max(summ, maxx)
            r = l

print(maxx, r)
        
        
