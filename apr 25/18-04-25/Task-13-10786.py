from ipaddress import *

ip1 = "151.172.115.121"
ip2 = "151.172.115.156"

for m in range(16, 33):
    net1 = ip_network(f"{ip1}/{m}", 0)
    net2 = ip_network(f"{ip2}/{m}", 0)
    if net1 != net2:
        if ip_address(ip1) not in (net1.network_address, net2.broadcast_address):
            if ip_address(ip2) not in (net2.network_address, net2.broadcast_address):
                print(m)


