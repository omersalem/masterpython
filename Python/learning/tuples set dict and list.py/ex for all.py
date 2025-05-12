devices = (
    ("FortiGate", "192.168.1.1", True),
    ("Cisco", "192.168.1.2", False)
)

allowed_ips = {"192.168.1.1", "192.168.1.3"}

for name, ip, status in devices:
    if ip in allowed_ips and status:
        print(f"{name} is allowed and running at {ip}")
    else:
        print(f"{name} is either blocked or offline")

print("Scanning ports...")
for port in range(80, 85):
    print(f"Scanning port {port}")

   #example of list
    devices = ["Firewall", "Switch", "Router"]
devices.append("Server")
print(devices[0])  # Firewall

#example of tuple
firewall_info = ("FortiGate", "192.168.1.1", "Running")
print(firewall_info[1])  # 192.168.1.1
#example of set
allowed_ips = {"192.168.1.1", "192.168.1.2"}
allowed_ips.add("192.168.1.3")
print(allowed_ips)
#example of dict
device = {"name": "FortiGate", "ip": "192.168.1.1", "status": "Running"}
device["model"] = "100E"
print(device["ip"])

