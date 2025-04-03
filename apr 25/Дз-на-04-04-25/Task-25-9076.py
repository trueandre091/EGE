from fnmatch import fnmatch


for n in range(2023, 10**9, 2023):
    summ = sum(map(int, str(n)))
    if fnmatch(str(n), "20*23") and summ % 7 == 0 and summ < 20:
        print(n)
