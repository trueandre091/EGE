from ipaddress import *

net = ip_network("98.81.154.195/255.252.0.0", False)

print(list(net.hosts())[-1])

