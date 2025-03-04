for A in range(10000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            a = (x - 3 * y) < A
            b = (y > 400)
            c = (x > 56)
            if not (a or b or c):
                break
        else:
            continue
        break
    else:
        print(A)
        break

# 54
