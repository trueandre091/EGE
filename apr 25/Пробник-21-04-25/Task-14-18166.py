n = 5**2025 + 5**200

a = []
for x in range(2, 2026):
    k = n - x
    c = 0
    while k:
        if k % 5 == 4: c += 1
        k //= 5
    a.append((x, c))

a = sorted(a, key=lambda i: (i[1], i[0]))

print(a[-10:])


