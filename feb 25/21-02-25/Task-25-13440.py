from fnmatch import fnmatch

for n in range(2658, 10**9, 2658):
    if fnmatch(str(n), "85?16*4"):
        print(n, n // 2658)



