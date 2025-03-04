from fnmatch import fnmatch

for n in range(1777, 10**10, 1777):
    if fnmatch(str(n), "21???68?79"):
        print(n, n//1777)