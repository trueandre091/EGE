
def pl(a, b, c):
    if a * b > c:
        return True
    return False

def f(x, y, A):
    return (not pl(x, y, A + 13)) <= (pl(28, y, 520) or pl(x, 25, 800))

for A in range(10000, -10000, -1):
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break


