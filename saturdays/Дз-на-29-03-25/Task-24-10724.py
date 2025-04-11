from string import digits, ascii_uppercase

with open("24_10724.txt") as file:
    data = file.readline()

alph = digits + ascii_uppercase

for i in alph[1:16]:
    data = data.replace(i, "*")

for i in alph[16:]:
    data = data.replace(i, " ")

data = data.split()
data_stripped = []
for i in data:
    while i[0] == "0":
        i = i[1:]
    data_stripped.append(i)

print(len(max(data_stripped, key=len)))





