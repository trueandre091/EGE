a = []
for n in range(4, 1000):
    s = "1" + n * "2"
    while "12" in s or "322" in s or "222" in s:
        s = s.replace("12", "2", 1)
        s = s.replace("322", "21", 1)
        s = s.replace("222", "3", 1)
    a.append(len(s))

print(max(a))
