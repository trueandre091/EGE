for n in range(4, 10000):
    s = "4" + n * "2"
    while "42" in s or "8222" in s or "2222" in s:
        s = s.replace("42", "2", 1)
        s = s.replace("8222", "24", 1)
        s = s.replace("2222", "8", 1)
    if sum(map(int, s)) == 110:
        print(n)
        break