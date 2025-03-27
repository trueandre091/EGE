for n in range(4, 10000):
    s = "1" + n * "2"
    while "12" in s or "32" in s or "22" in s:
        s = s.replace("12", "22", 1)
        s = s.replace("32", "211", 1)
        s = s.replace("22", "3", 1)
    summ = sum(map(int, s))
    if summ % 6 == 0:
        print(n)
        break