a = []
for n in range(4, 2000):
    s = n * "3" + "5"
    while "23" in s or "5333" in s or "33333" in s:
        s = s.replace("23", "3", 1)
        s = s.replace("5333", "32", 1)
        s = s.replace("33333", "55", 1)

    summ = sum(map(int, s))
    a.append(summ)

print(min(a))








