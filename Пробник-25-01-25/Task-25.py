from fnmatch import fnmatch
from sympy import divisors

ans = []
for n in range(65000, 10**5):
    div = divisors(n)
    ch_div = []
    for div_n in div:
        if div_n % 2 == 0:
            ch_div.append(div_n)

    if len(ch_div) >= 4:
        ans.append((n, sum(ch_div)))

for i in range(7):
    print(ans[i][0], ans[i][1])



