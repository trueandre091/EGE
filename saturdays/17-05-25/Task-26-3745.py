with open("26_3745.txt") as f:
    n = int(f.readline())
    data = [tuple(map(int, l.split())) for l in f]

data = sorted(data, key=lambda x: (x[0], x[1]))
ans = []
lines = [0] * 100

# p1 p2
# p3 p4

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i + 1]
    p3, p4 = (p1[0] + 1, p1[1]), (p2[0] + 1, p2[1])
    if p3 in data and p4 in data:
        if p1[0] == p2[0]:
            u_1, u_2 = (p1[0] - 1, p1[1]), (p2[0] - 1, p2[1])
            d_3, d_4 = (p3[0] + 1, p3[1]), (p4[0] + 1, p4[1])
            l_1, l_3 = (p1[0], p1[1] - 1), (p3[0], p3[1] - 1)
            r_2, r_4 = (p2[0], p2[1] + 1), (p4[0], p4[1] + 1)
            near_cube = [u_1, u_2, d_3, d_4,
                         l_1, l_3, r_2, r_4]
            if all(p not in data for p in near_cube):
                ans.append(p1)
                lines[p1[0]] += 1
                lines[p1[0] + 1] += 1

print(len(ans))
print(lines.index(max(lines)))






