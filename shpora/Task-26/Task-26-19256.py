with open("26_19256.txt") as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

students = dict()
for i in data:
    if i[0] not in students: students[i[0]] = {i[1]}
    else: students[i[0]].add(i[1])

ans = []
for student, tasks in students.items():
    tasks = sorted(tasks)
    max_c = 1
    c = 1
    for i in range(len(tasks) - 1):
        if tasks[i] + 1 == tasks[i + 1]:
            c += 1
        else:
            c = 1
        max_c = max(c, max_c)
    ans.append((student, max_c))

best = sorted(ans, key=lambda x: (-x[1], x[0]))
print(best[0])


