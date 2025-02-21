from fnmatch import fnmatch

ans = []

for n in range(2023, 10**8, 2023):
    if fnmatch(str(n), "3?1*57"):
        ans.append((n, n // 2023))

for i in ans:
    print(i[0], i[1])


