with open("24-input.txt") as f:
    data = f.readline()

# max_s = ()
# for i in range(1000):
#     s = "RSQ" * i
#     k = data.find(s)
#     if k != -1:
#         max_s = (k, k + len(s), i)
# i = 17

print(data.count("RSQ" * 17))

s = "RSQ" * 17

max_l = -1
for i in ["R", "RS", "RSQ"]:
    for j in ["Q", "SQ", "RSQ"]:
        k = data.find(j + s + i)
        print(k, j + s + i)
        if k != -1:
            max_l = max(max_l, len(j + s + i))
print(max_l)

