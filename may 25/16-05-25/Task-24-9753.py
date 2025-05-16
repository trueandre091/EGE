with open("24_9753.txt") as f:
    data = f.readline()

data = data.split("Y")

ans = []
for i in range(len(data) - 150):
    s = "Y".join(data[i:i+151])
    ans.append(len(s))

print(max(ans))

