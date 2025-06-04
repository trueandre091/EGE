from string import *

alph = digits + ascii_lowercase

for x in alph[:23]:
    num = int(f"7{x}38596", 23) + int(f"14{x}36", 23) + int(f"61{x}7", 23)
    if num % 22 == 0:
        print(num // 22)
        break