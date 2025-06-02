def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res


a = []
for N in range(3, 10000):
    NN = f(N)
    if N % 3 == 0:
        NN += NN[-2:]
    else:
        NN += f(N % 3 * 3)
    R = int(NN, 3)
    if R <= 150:
        a.append(N)

print(max(a))
