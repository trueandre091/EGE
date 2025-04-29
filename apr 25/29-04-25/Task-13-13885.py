from ipaddress import *

def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("1") >= ip[16:].count("1")

for m in range(31):
    net = ip_network(f"238.51.1.202/{m}", 0)
    if all(f(i) for i in net):
        ip = ip_address("238.51.1.202")
        if ip not in (net.broadcast_address, net.network_address):
            print(m)


