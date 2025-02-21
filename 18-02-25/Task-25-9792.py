from fnmatch import fnmatch

for n in range(120076 - 120076 % 1923, 10**8, 1923):
    if fnmatch(str(n), "1*2??76"):
        print(n, n // 1923)



