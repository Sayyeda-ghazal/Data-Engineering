from collections import Counter

code = '192.168.1.10 - - [27/Oct/2026:10:15:32 +0000] "GET /api/users HTTP/1.1" 200 1024'
parts = code.split()
print(parts)

ip = parts[0]
endpoint = parts[6]
status_code = int(parts[8])

print("IP Address", ip)
print("Endpoint", endpoint)
print("Status code", status_code)

ips = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.11"
]

unique_ips = set(ips)
print("Unique Ips:", len(unique_ips))

endpoints = [
    "/api/users",
    "/api/products",
    "/api/users",
    "/api/orders",
    "/api/products",
    "/api/users"
]

repeat_endpnts = Counter(endpoints)
print("Unique Endpoints:", repeat_endpnts)

common_endpnts = repeat_endpnts.most_common(2)
print("Commmon Endpoints:", common_endpnts)
