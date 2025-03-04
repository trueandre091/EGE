from ipaddress import ip_address, ip_network

for A in range(256):
    net = ip_network(f"192.214.{A}.184/255.255.255.224", 0)
    for ip in net:
        if f"{ip:b}".count("1") <= 15:
            break
    else:
        print(A)
        break