from ipaddress import ip_address, ip_network

ip1 = "123.20.103.136"
ip2 = "123.20.103.151"

for mask in range(33):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if ip1 == str(net1.broadcast_address) or ip1 == str(net1.network_address) or ip2 == str(net2.network_address) or ip2 == str(net2.broadcast_address):
        continue
    if net1 != net2:
        print(mask)
        mask_ip = ip_network(f"255.255.255.255/{mask}", 0)
        print(mask_ip)
