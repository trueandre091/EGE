from fnmatch import fnmatch

for n in range(2902302310 - 2902302310 % 1984, 10**10, 1984):
    if fnmatch(str(n), "[2468]9?23?*23[13579][02468]"):
        print(n, n // 1984)

