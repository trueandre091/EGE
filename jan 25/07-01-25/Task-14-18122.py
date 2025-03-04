for x in range(1, 5555):
    num = 5**150 + 5**135 - x
    res = ""
    while num:
        res = str(num % 5) + res
        num //= 5
    if res.count("4") == 134:
        print(x)