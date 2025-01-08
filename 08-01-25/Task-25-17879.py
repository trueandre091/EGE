from sympy import factorint

c = 0
for i in range(800000, 10**7):
    if c == 5:
        break
    dels = list(factorint(i).keys())
    m = max(dels) + min(dels) if dels else 0
    if str(m)[-1] == "4":
        print(i, m)
        c += 1

# 800007 284
# 800013 266674
# 800019 8084
# 800035 3024
# 800039 7584
