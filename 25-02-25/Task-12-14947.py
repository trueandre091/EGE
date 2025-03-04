a = []
for n in range(9999, 2, -1):
    s = "1" + n * "9"
    while "19" in s or "49" in s or "999" in s:
        s = s.replace("19", "9", 1)
        s = s.replace("49", "91", 1)
        s = s.replace("999", "4", 1)
    summ = sum(map(int, s))
    a.append(summ)


print(max(a))



















