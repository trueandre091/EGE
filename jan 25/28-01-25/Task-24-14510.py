from string import ascii_uppercase

with open("24-input.txt") as f:
    data = f.readline()

gl = "EYUIOA"
sogl = set(ascii_uppercase) - set(gl)

for i in gl:
    data = data.replace(i, "*")

for i in sogl:
    data = data.replace(i, "#")

data = data.replace("##*", "!")
data = data.replace("*", "#")
data = data.split("!")

minn = 10**10
for i in range(len(data) - 499):
    s = data[i:i+499]
    l = sum(len(k) for k in s)
    if minn > l:
        minn = l


print(minn + 500 * 3)













