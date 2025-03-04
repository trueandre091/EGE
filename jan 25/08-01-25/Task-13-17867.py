from ipaddress import ip_address, ip_network

mask = "255.255.248.0"
net = ip_network(f"172.16.168.0/{mask}", strict=False)

c = 0
for ip in net:
    if '{:#b}'.format(ip_address(ip)).count("1") % 5 != 0:
        c += 1

print(c)

# 1663
