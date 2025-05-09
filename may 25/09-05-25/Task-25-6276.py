from fnmatch import fnmatch

for n in range(2023, 10**10, 2023):
    summ = sum(map(int, str(n)))
    if summ == 22:
        if fnmatch(str(n), "1?1?1?1*1"):
            print(n)


