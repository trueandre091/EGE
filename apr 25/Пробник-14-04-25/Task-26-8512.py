with open("26_8512.txt") as f:
    K = int(f.readline())
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

ans = 0
correct = []
slots = [0] * K

for t in range(1, 1442):
    pot = [p for p in data if p[0] == t]

    for i in range(len(slots)):
        if slots[i] == t + 1:
            slots[i] = 0
            ans += 1

    if pot and 0 in slots:
        i0 = slots.index(0)
        slots[i0] = pot[0][1]
        add = pot[0] + [i0]
        correct.append(add)

print(ans)
print(correct, len(correct))





