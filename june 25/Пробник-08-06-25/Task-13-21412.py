from ipaddress import *

net = ip_network("143.168.72.213/255.255.255.240", False)
print(max(net.hosts()))


