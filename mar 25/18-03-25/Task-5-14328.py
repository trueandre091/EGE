from string import ascii_lowercase, digits
alph = digits + ascii_lowercase

def f(n):
    res = ""
    while n:
        res = alph[n % 12] + res
        n //= 12
    return res

a = []
for N in range(1, 100000):
    NN = f(N)
    if N % 3 == 0:
        NN = "1" + NN + "b"
    else:
        NN = "2" + NN + "0"
    R = int(NN, 12)
    if R < 1996:
        a.append(R)

print(max(a))