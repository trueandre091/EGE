with open("24-input.txt") as f:
    data = f.readline().strip("*+")

from string import digits

data = data.replace("+", "*")

while "**" in data:
    data = data.replace("**", " ")

for i in "13579": data = data.replace(i, "1")
for i in "02468": data = data.replace(i, "2")

while " *1" in data: data = data.replace(" *1", " 1")
while " *2" in data: data = data.replace(" *2", " 2")
while "1* " in data: data = data.replace("1* ", "1 ")
while "2* " in data: data = data.replace("2* ", "2 ")

# for i in "0123456789":
#     while f" *{i}" in data: data = data.replace(f" *{i}", f" {i}")
#     while f"{i}* " in data: data = data.replace(f"{i}* ", f"{i} ")

data = data.split()

print(len(data))

a = []
for s in data:
    for i in s.split("*"):
        if int(i) % 2 != 0:
            break
    else:
        a.append(s)

print(len(max(a, key=len)))





