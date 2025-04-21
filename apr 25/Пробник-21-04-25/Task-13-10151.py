from ipaddress import *

ip = ip_address("111.81.208.27")

for m in range(33):
    net = ip_network(f"111.81.208.27/{m}", 0)
    if str(net.network_address) == "111.81.192.0":
        if ip not in (net.network_address, net.broadcast_address):
            print(min(m - 16, 8))

ip = ip_address("111.81.208.27")
net = ip_address("111.81.192.0")
print(f"{int(ip):032b}")
print(f"{int(net):032b}")




