from string import ascii_lowercase, digits
alph = digits + ascii_lowercase

for x in alph[:25]:
    n1 = int(f"11353{x}12", 25)
    n2 = int(f"135{x}21", 25)
    summ = n1 + n2
    if summ % 24 == 0:
        print(x, summ / 24)

# m 266249847
