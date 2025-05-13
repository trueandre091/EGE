with open("24_2942.txt") as f:
    data = f.readline()

data = data.replace("AB", "*").replace("AC", "*")

for i in "ABC":
    data = data.replace(i, " ")
data = data.split()

print(len(max(data, key=len)))


