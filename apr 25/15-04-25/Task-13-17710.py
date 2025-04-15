from ipaddress import *

net = ip_network("214.187.224.0/255.255.224.0")

c = 0
for i in net:
    ip = f"{int(i):032b}"
    n1 = ip.count("1") % 6 != 0
    n2 = ip[-4:] == "1000"
    if n1 and n2:
        c += 1

print(c)


