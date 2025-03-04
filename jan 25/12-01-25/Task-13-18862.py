from ipaddress import ip_address, ip_network

net = ip_network(f"172.140.68.0/255.255.248.0", 0)

c = 0
for ip in net:
    if f"{ip:b}".count("0") > 15:
        c += 1

print(c)
