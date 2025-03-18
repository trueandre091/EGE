def f(n):
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            return False
    return True


for n in range(4, 1000):
    s = ">" + 25 * "0" + "1" * n + 25 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        s = s.replace(">1", "22>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "1>", 1)
    if f(sum(map(int, s[:-1]))):
        print(n)
        break