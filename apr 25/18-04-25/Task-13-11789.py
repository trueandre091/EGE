from ipaddress import *

def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("1") <= ip[16:].count("1")

for m in range(16, 25):
    net = ip_network(f"99.8.254.232/{m}", 0)
    if all(f(i) for i in net):
        print(m)



