for A in range(1, 10000):
    for x in range(1, 1000):
        f1 = (A + x) > (700 - A)
        f2 = (A % 100) + (100 % x) > 50
        if not (f1 and f2):
            break
    else:
        print(A)
        break
