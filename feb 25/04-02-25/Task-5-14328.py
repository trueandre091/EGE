from string import digits, ascii_lowercase

alph = digits + ascii_lowercase


def f(n):
    res = ""
    while n:
        res = alph[n % 12] + res
        n //= 12
    return res

c = []
for N in range(1, 10000):
    NN = f(N)
    if N % 3 == 0:
        NN = "1" + NN + "b"
    else:
        NN = "2" + NN + "0"
    R = int(NN, 12)
    if R < 1996:
        c.append(R)

print(max(c))