
def f(x):
    return ((x % 2 == 0) <= (not (x % 3 == 0))) or ((x + A) >= 80)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break