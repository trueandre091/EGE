from sympy import factorint, divisors

c = 0
for i in range(800001, 10**7):
    if c == 5:
        break
    dels = divisors(i)[1:-1]
    m = max(dels) + min(dels) if len(dels) >= 2 else 0
    if str(m)[-1] == "4":
        print(i, m)
        c += 1

# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554
