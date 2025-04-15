with open("24_19149.txt") as f:
    data = f.readline()

st_i = 0
en_i = 0
s = []
for i in range(len(data) - 1):
    if data[i] == "(":
        st_i = i
        for j in range(st_i + 1, len(data)):
            if data[j] == ")":
                en_i = j
                break
            if data[j] == "(":
                st_i = 0
                break
        if st_i != 0 or en_i != 0:
            s.append((st_i, en_i))
        st_i, en_i = 0, 0

avail = []
for st_i, en_i in s:
    try:
        res = eval(data[st_i + 1:en_i])
        if res % 2 == 0:
            avail.append((en_i - st_i + 1, st_i, en_i))
    except:
        continue

print(max(avail))
print(data[4536355:4536433])




