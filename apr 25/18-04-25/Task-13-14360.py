from ipaddress import *

ip1 = "153.202.16.37"

for m in range(33):
    net = ip_network(f"153.202.16.32/{m}", 0)
    if ip_address(ip1) in net:
        if ip_address(ip1) not in (net.network_address, net.broadcast_address):
            print(m)

