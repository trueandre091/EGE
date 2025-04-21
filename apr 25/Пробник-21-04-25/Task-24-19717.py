with open("24_19717.txt") as f:
    data = f.readline()

data = data.split("M")

a = []
for i in range(len(data) - 278):
    s = "".join(data[i:i+279])
    a.append(len(s) + 278)

print(max(a))


