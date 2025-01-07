from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

for x in alph[1:35]:
    num1 = int(f"6{x}qr{x}", 35)
    num2 = int(f"{x}59sh", 35)
    num3 = int(f"ph{x}69yw", 35)
    summ = num1 + num2 + num3
    counts = [0] * 10
    for i in str(summ):
        counts[int(i)] += 1
    counts = counts[::-1]
    maxx = 9 - counts.index(max(counts))
    if summ % maxx**2 == 0:
        print(summ // maxx**2)

#