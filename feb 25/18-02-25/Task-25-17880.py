from fnmatch import fnmatch

ans = []
for n in range(1917, 10**10, 1917):
    if fnmatch(str(n), "3?12?14*5"):
        ans.append((n, n // 1917))

for i in ans:
    print(i[0], i[1])

