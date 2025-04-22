from ipaddress import *

ip1 = ip_address("118.187.59.255")
ip2 = ip_address("118.187.65.115")

for m in range(33):
    net1 = ip_network(f"118.187.59.255/{m}", 0)
    net2 = ip_network(f"118.187.65.115/{m}", 0)
    if net1 != net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                print(m)






