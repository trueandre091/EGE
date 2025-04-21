from ipaddress import *

ip1 = "218.48.192.56"

for m in range(24):
    net = ip_network(f"{ip1}/{m}", 0)
    if str(net.network_address) == "218.48.192.0":
        print((m*"1" + "0"*(32-m))[16:25])



