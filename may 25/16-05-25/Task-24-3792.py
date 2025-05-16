with open("24_3792.txt") as f:
    data = f.readline().strip()

data = data.replace("D", " ").replace("E", " ")
data = data.split()

print(len(max(data, key=len)))

