from ipaddress import *

ip1 = "200.154.190.12"
ip2 = "200.154.184.0"
ipp1 = ip_address(ip1)
ipp2 = ip_address(ip2)

for m in range(14, 31):
    net1 = ip_network(f"{ip1}/{m}", 0)
    net2 = ip_network(f"{ip2}/{m}", 0)
    if net1 == net2:
        if ipp1 not in (net1.network_address, net1.broadcast_address):
            if ipp2 not in (net1.network_address, net1.broadcast_address):
                print(m)


