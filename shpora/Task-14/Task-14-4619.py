n = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550

c0 = 0
while n:
    if n % 7 == 0: c0 += 1
    n //= 7

print(c0)

