from ipaddress import *

ip1 = "216.54.187.235"
ip2 = "216.54.174.128"

for m in range(16, 33):
    net1 = ip_network(f"{ip1}/{m}", 0)
    net2 = ip_network(f"{ip2}/{m}", 0)
    if net1 != net2:
        if ip_address(ip1) not in (net1.broadcast_address, net1.network_address):
            if ip_address(ip2) not in (net2.broadcast_address, net2.network_address):
                print(m)



