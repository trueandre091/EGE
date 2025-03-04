from fnmatch import fnmatch

ans = []

for n in range(161, 10**8, 161):
    if fnmatch(str(n), "12*4?65"):
        ans.append((n, n // 161))

for i in ans:
    print(i[0], i[1])
