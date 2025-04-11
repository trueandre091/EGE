from ipaddress import *

ip1 = "193.175.175.231"
ip2 = "193.175.176.118"

for m in range(33):
    net1 = ip_network(f"{ip1}/{m}", False)
    net2 = ip_network(f"{ip2}/{m}", False)
    if net1 != net2:
        print(m)


