

for p in range(16, 37):
    num1 = int("17496", p)
    num2 = int("91f83", p)
    num3 = int("d9543", p)
    summ = num1 + num2 + num3
    if summ % 12 == 0:
        print(summ // 12)
