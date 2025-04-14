for x in range(1, 111):
    n1 = x * 111**3 + 3 * 111**2 + 2 * 111 + 1
    n2 = 1 * 211**3 + 7 * 211**2 + x * 211 + 4
    summ = n1 + n2
    if summ % 111 == 0:
        print(x, summ / 111)