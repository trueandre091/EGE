from ipaddress import *

def c(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("1") >= ip[16:].count("1")

for m in range(16, 25):
    net = ip_network(f"127.63.67.1/{m}", False)
    if all(c(i) for i in net):
        print(m)


