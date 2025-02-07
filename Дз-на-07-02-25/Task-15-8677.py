from itertools import combinations

def dell(n, m):
    return n % m == 0

def f(x):
    B = 80 <= x <= 100
    return dell(x, 17) <= ((not B) or (A < (x + 30)))

ans = []
line = [i / 5 for i in range(10 * 5, 120 * 5)]

for A in line:
    if all(f(x) for x in line):
        ans.append(A)

print(max(ans))

# 114.8 -> 114
