with open("17_6089.txt") as f:
    data = [int(i) for i in f]

maxx = abs(max(i for i in data if str(i)[-1] == "2"))

ans = []
for n in data:
    nn = abs(n)
    if nn % 3 == 0:
        if nn % 7 != 0 and nn % 17 != 0:
            if maxx % nn == 0:
                ans.append(n)

print(len(ans), max(ans))




