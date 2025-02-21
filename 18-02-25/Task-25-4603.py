from fnmatch import fnmatch

ans = []

for n in range(141, 10**8, 141):
    if fnmatch(str(n), "1234*7"):
        ans.append((n, n // 141))

for i in ans:
    print(i[0], i[1])