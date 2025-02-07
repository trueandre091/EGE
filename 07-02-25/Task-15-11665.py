

def mod(x, y):
    return x % y

def f(x):
    return ((A + x) > (700 - A)) and ((mod(A, 100) + mod(100, x)) > 50)

for A in range(1, 10000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break




