from ipaddress import *

i1 = "200.154.190.12"
i2 = "200.154.184.0"

a = []
for m in range(15, 31):
    net1 = ip_network(f"{i1}/{m}", False)
    net2 = ip_network(f"{i2}/{m}", False)
    if net1 == net2:
        ip1 = ip_address(i1)
        ip2 = ip_address(i2)
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                a.append(m)

print(max(a))

