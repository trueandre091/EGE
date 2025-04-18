from ipaddress import *

ip1 = "157.127.172.56"
ip2 = "157.127.191.78"

for m in range(33):
    net1 = ip_network(f"{ip1}/{m}", 0)
    net2 = ip_network(f"{ip2}/{m}", 0)
    if net1 != net2:
        if ip_address(ip1) in net1.hosts() and ip_address(ip2) in net2.hosts():
            print(m)



