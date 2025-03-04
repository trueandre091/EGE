from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

for x in alph[:26]:
    n1 = int(f"27{x}98876", 26)
    n2 = int(f"26{x}51", 26)
    n3 = int(f"15{x}47", 26)
    n4 = int(f"62{x}5", 26)
    summ = n1 + n2 + n3 + n4
    if summ % 25 == 0:
        print(x, summ // 25)
