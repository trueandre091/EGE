def b(n):
    n = int(n)
    return bin(n)[2:].zfill(8)

with open("26_3902.txt") as f:
    n = f.readline()
    data = ["".join(list(map(b, i.split()))) for i in f]

k = {}
for ip in data:
    net = ip[:19]
    if net not in k:
        k[net] = [set(ip[19:]), 1]
    else:
        k[net][0].append(ip[19:])
        k[net][1] += 1

    k[net][0] = list(set(k[net][0]))

maxx = ("", 0)
for net, ips in k.items():
    if ips[1] > maxx[1]:
        maxx = (net, ips)


print(maxx)


