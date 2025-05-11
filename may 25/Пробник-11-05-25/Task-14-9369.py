from string import *
alph = digits + ascii_lowercase

for x in alph[:16]:
    for y in alph[:16]:
        num = int(f"27a{x}23", 16) + int(f"8{y}e5d2", 16)
        if num % 5 == 0:
            print(int(x, 36) + int(y, 36))
