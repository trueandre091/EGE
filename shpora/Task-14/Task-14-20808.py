n = 7**170 + 7**100
a = []
for x in range(1, 2030):
    num = n - x
    c0 = 0
    while num:
        if num % 7 == 0: c0 += 1
        num //= 7
    a.append((c0, x))

a = sorted(a, key=lambda x: (x[0], x[1]))
print(a[-1])
