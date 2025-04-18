from ipaddress import *

ip1 = "121.171.5.70"
ip2 = "121.171.5.107"

print(f"{int(ip_address(ip1)):032b}")
print(f"{int(ip_address(ip2)):032b}")


