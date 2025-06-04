n = 4**210+ 4**110
a = []
for x in range(1, 3000):
    num = n - x
    c0 = 0
    while num:
        if num % 4 == 0:
            c0 += 1
        num //= 4
    a.append((c0, x))

a = sorted(a, key=lambda x: (x[0], -x[1]))
print(a[-1])