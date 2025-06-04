from ipaddress import *

i1 = "95.24.2.9"
i2 = "95.24.3.10"

a = []
for m in range(15, 31):
    net1 = ip_network(f"{i1}/{m}", False)
    net2 = ip_network(f"{i2}/{m}", False)
    if net1 != net2:
        ip1 = ip_address(i1)
        ip2 = ip_address(i2)
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                a1 = net1.num_addresses / 2 - 1
                a2 = net2.num_addresses / 2 - 1
                a.append(a1)
                a.append(a2)

print(max(a))
