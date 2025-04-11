from ipaddress import *

ip1 = "112.117.107.70"
ip2 = "112.117.121.80"

for m in range(33):
    net1 = ip_network(f"{ip1}/{m}", False)
    net2 = ip_network(f"{ip2}/{m}", False)
    if net1 == net2:
        print(m)

