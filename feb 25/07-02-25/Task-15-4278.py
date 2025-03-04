from itertools import combinations

def dell(n, m):
    return n % m == 0

def f(x):
    return dell(A, 12) and (dell(530,x) <= ((not dell(A, x)) <= (not (dell(170, x)))))

a = 0
for A in range(1, 1001):
    if all(f(x) for x in range(1, 10000)):
        a += 1
print(a)

