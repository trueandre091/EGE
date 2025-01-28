def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

a = []
for N in range(1, 10000):
    NN = f(N)
    summ = sum(map(int, str(NN)))
    if summ % 3 == 0:
        NN += "212"
    else:
        NN += f(summ * 2)
    R = int(NN, 3)
    if R > 490:
        a.append(R)

print(min(a))
