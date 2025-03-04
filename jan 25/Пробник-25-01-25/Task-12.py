def pros(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for n in range(2, 1000):
    if not pros(n):
        continue

    s = ">" + 21 * "0" + n * "1" + 11 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s: s = s.replace(">1", "22>", 1)
        if ">2" in s: s = s.replace(">2", "2>", 1)
        if ">0" in s: s = s.replace(">0", "1>", 1)

    summ = sum(map(int, s[:-1]))
    if summ % n == 0:
        print(n)











