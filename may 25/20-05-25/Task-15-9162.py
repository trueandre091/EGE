def area(a, b, c):
    return a * b * 0.5 > c

def f(x, y):
    return (not area(x, y, A + 13)) <= area(28, y, 520) or area(x, 25, 800)

for A in range(-100, 100)[::-1]:
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break







