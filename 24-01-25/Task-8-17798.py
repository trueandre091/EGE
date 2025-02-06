from itertools import product

alph = sorted("МИНУС")
sogl = "МНС"

a = []
for pos, i in enumerate(product(alph, repeat=4), 1):
    i = "".join(i)
    sogl_c = sum(j in sogl for j in i)
    gl_c = sum(j not in sogl for j in i)
    if sogl_c >= gl_c:
        a.append(pos)

print(a[-1])

# 619
