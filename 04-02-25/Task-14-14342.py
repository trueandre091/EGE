from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for p in range(25, 37):
    u = int("bo", p) + int("om", p) + int("bl4", p) == int("cng", p)
    if u:
        print(p)