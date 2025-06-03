with open("26_9793.txt") as f:
    N = int(f.readline())
    data = []
    c = 0
    for i in f:
        i = i.split()
        c += 1
        info1 = {
            "time": int(i[0]), "type": 0, "detail": c
        }
        info2 = {
            "time": int(i[1]), "type": 1, "detail": c
        }
        data.append(info1)
        data.append(info2)

# types: 0 - шлифовка; 1 - окрашивание

transp = [[]] * N
last = 0

while data:
    data = sorted(data, key=lambda x: x["time"])
    minn = data[0]

    detail_parts = [i for i in data if i["detail"] == minn["detail"]]
    times = (detail_parts[0]["time"], detail_parts[1]["time"])

    detail = {
        "detail": minn["detail"],
        "times": times if detail_parts[0]["type"] == 0 else times[::-1]
    }

    if minn["type"] == 0:
        for i in range(len(transp)):
            if not transp[i]:
                transp[i] = detail
                break
    else:
        for i in range(len(transp))[::-1]:
            if not transp[i]:
                transp[i] = detail
                break

    last = detail

    data.remove(detail_parts[0])
    data.remove(detail_parts[1])

print(last)
print(transp.index(last))
