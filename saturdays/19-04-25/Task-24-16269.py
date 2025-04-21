with open("24_16269.txt") as f:
    data = f.readline()

for i in "TUVW":
    data = data.replace(i, " ")

while "XXX" in data: data = data.replace("XXX", "XX XX")
while "YYY" in data: data = data.replace("YYY", "YY YY")
while "ZZZ" in data: data = data.replace("ZZZ", "ZZ ZZ")

data = data.split()

print(len(max(data, key=len)))




