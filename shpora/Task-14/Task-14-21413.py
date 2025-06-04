from string import *
alph = digits + ascii_lowercase
for x in alph[:21]:
    num = int(f"82934{x}2", 21) + int(f"2924{x}{x}7", 21) + int(f"67564{x}8", 21)
    if num % 20 == 0:
        print(x, num // 20)