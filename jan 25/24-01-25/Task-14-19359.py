from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:22]:
    n1 = int(f"a23{x}ac0", 22)
    n2 = int(f"gb{x}21670", 22)
    if (n1 + n2) % 21 == 0:
        print(x, (n1 + n2) // 22)

# 1923296823
