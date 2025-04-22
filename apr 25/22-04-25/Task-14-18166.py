n = 5**2025 + 2**200

a = []
for x in range(2, 2026):
    num = n - x
    c = 0
    while num:
        if num % 5 == 4: c += 1
        num //= 5

    a.append((c, x))

a = sorted(a, key=lambda x: (x[0], x[1]))

print(a[-1])



