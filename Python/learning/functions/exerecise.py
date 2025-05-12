def get_ip_by_type(devices, type_name):
    ips = []
    for device in devices:
        if device["type"]== type_name:
            ips.append(device["ip"])
    if ips:
        return ips
    else: return "Device not found"

    


devices = [{"name": "firewall","ip":"192.168.1.1","type":"firewall"},
          {"name": "switch","ip":"192.168.1.2","type":"firewall"},
          {"name": "router","ip":"10.0.0.1","type":"router"}]
ips=[]
ips=get_ip_by_type(devices, "firewall")
for ip in ips:
    print(f"IP address of firewall: {ip}")

#------------------------------------------------------------------------------------------------------------

def filter_devices_by_status(devices, status):
    matched_devices=[]

    for device in devices:
    
        if device['status']=="running":
           matched_devices.append(device['name'])
        
    return matched_devices

devices=[
    {"name": "Firewall1", "status": "running"},
    {"name": "Switch1", "status": "stopped"},
    {"name": "Router1", "status": "running"}
]


running_devices=filter_devices_by_status(devices, "running")

for device in running_devices:
    print(f"Device {device} is running")

# This code defines a function to filter devices by their status 
# (e.g., "running") and prints the names of devices that match the specified status.
