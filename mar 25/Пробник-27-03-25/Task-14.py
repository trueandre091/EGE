n = 2**2025 + 2**2024 - 2**2021

a = []
for x in range(1, 2030):
    nn = n - x
    c = 0
    while nn:
        if nn % 4 == 0:
            c += 1
        nn //= 4
    a.append((c, x))

a = sorted(a, key=lambda x: (x[0], x[1]))
print(a[-1])
print(a)