with open("24_19254.txt") as f:
    original = f.readline().strip()

data = original.split("FSRQ")

a = []
for i in range(len(data) - 80):
    s = "SRQ" + "FSRQ".join(data[i:i+81]) + "FSR"
    a.append(s)

maxx = max(a, key=len)
print(len(maxx))
print(maxx in original)



