from string import digits, ascii_lowercase


alph = digits + ascii_lowercase

for x in alph[:25]:
    num1 = int(f"11353{x}12", 25)
    num2 = int(f"135{x}21", 25)
    summ = num1 + num2
    if summ % 24 == 0:
        print(x, summ // 24)



