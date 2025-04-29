from ipaddress import *

for m in range(16, 31):
    net1 = ip_network(f"122.117.107.70/{m}", 0)
    net2 = ip_network(f"122.117.121.80/{m}", 0)
    if net1 == net2:
        if ip_address("122.117.107.70") not in (net1.network_address, net1.broadcast_address):
            if ip_address("122.117.121.80") not in (net1.network_address, net1.broadcast_address):
                print(net1.num_addresses)





