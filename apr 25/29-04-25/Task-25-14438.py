from fnmatch import fnmatch


for n in range(86513, 10**12, 86513):
    if fnmatch(str(n), "17*46??8"):
        summ = sum(map(int, str(n)))
        if summ**0.5 % 1 == 0:
            print(n, n // 86513)


