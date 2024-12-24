from string import digits, ascii_lowercase

def c(n, sys):
    alph = digits + ascii_lowercase
    res = ""
    while n:
        res = alph[n % sys] + res
        n //= sys
    return res

a = []
for N in range(1, 10000):
    NN = c(N, 3)
    if N % 3 == 0:
        NN += NN[-2:]
    else:
        NN += c(sum(map(int, NN)), 3)
    R = int(NN, 3)
    if R > 220 and R % 2 == 0:
        a.append(R)

print(min(a))