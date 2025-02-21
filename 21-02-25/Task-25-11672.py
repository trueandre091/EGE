from fnmatch import fnmatch

for n in range(21025, 10**10, 21025):
    if fnmatch(str(n), "12*34?5"):
        ch = [i for i in str(n) if int(i) % 2 == 0]
        if len(ch) == len(str(n)) - len(ch):
            print(n, n// 21025)

