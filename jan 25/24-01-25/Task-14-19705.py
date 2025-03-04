n = 43**56 + 113**841

a = []
for x in range(1, 2005):
    num = n - x
    chet = ""
    c_ch = 0
    c_nech = 0
    c_2 = 0
    while num:
        if num % 4 in [0, 2]:
            c_ch += 1
        if num % 4 in [1, 3]:
            c_nech += 1
        if num % 4 == 2:
            c_2 += 1
        num //= 4

    if c_ch % 2 == 0 and c_nech % 2 == 0 and c_2 <= 712:
        a.append(x)

print(max(a))

# 2001
