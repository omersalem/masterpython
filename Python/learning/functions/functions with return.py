def is_private_ip(ip):
    if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172.16."):
        return True
    else:
        return False

ip = "192.168.1.1"
if is_private_ip(ip):
    print(f"The IP {ip} is a private IP.")
else:
    print(f"The IP {ip} is a public IP.")
#------------------------------------------------------------------------------------------------------------
#example 2
def get_device_status(devices, name):
    for device in devices:
        if device["name"] == name:
            return device["status"]
    return "Device not found"

devices = [
    {"name": "Firewall1", "status": "running"},
    {"name": "Switch1", "status": "stopped"}
]

status = get_device_status(devices, "Switch1")
print(f"Status: {status}")