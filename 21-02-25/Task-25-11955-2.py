from fnmatch import fnmatch

for n in range(1021574 - 1021574 % 133, 10**10, 133):
    if int(str(n)[1]) % 2 != 0:
        continue


