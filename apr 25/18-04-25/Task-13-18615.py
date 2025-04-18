from ipaddress import *

ip1 = "143.131.211.37"

for m in range(33):
    net = ip_network(f"{ip1}/{m}", 0)
    c = 0
    if ip_address(ip1) not in (net.broadcast_address, net.network_address):
        for i in net:
            ip = f"{int(i):032b}"
            if ip.count('1') == 10:
                c += 1
            if c > 15:
                break
        else:
            if c == 15:
                print(m)


