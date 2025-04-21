from ipaddress import *

ip1 = "127.63.67.1"

def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("1") >= ip[16:].count("1")

for m in range(16, 25):
    net = ip_network(f"{ip1}/{m}", 0)
    if ip_address(ip1) not in (net.network_address, net.broadcast_address):
        if all(f(i) for i in net):
            print(m)




