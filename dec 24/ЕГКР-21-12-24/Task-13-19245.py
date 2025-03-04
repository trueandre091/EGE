from ipaddress import ip_address, ip_network

ip = ip_address("218.194.82.148")
net_mask = "255.255.255.192"

net = ip_network(f"{ip}/{net_mask}", strict=False)
ip_max = net.broadcast_address - 1

print(ip_max)

# 21819482190
