from ipaddress import *


def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("0") <= ip[16:].count("0")

for A in range(256):
    net = ip_network(f"217.109.{A}.94/255.255.254.0", 0)
    ipn = ip_address(f"217.109.{A}.94")
    if ipn not in (net.broadcast_address, net.network_address):
        if all(f(i) for i in net):
            print(A)


