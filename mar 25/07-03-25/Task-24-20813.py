with open("24_20813.txt") as f:
    data = f.readline()

data = data.replace("-", "*")
data = data.replace("7", "8").replace("9", "8")

data = data.replace("**", " ").replace("* ", " ").replace(" *", " ")

for i in range(1, 10):
    data = data.replace(f"*{'0' * i}8", "*0 8")
    data = data.replace(f" {'0' * i}8", " 8")

for i in range(2, 10):
    data = data.replace(f"*{'0' * i}*", "*0 0*")


data = data.split()
print(len(max(data, key=len)))


