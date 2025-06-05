from fnmatch import fnmatch

for n in range(2024, 10**10, 2024):
    if fnmatch(str(n), "1?2157*4"):
        print(n, n//2024)

