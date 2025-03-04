from fnmatch import fnmatch

for n in range(1035954 - 1035954 % 6437, 10**10, 6437):
    if fnmatch(str(n), "1?3*5*954"):
        print(n, n // 6437)


