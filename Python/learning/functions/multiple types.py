devices = [
    {"name": "Firewall", "ip": "192.168.1.1", "status": "running"},
    {"name": "router", "ip": "192.168.1.2", "status": "stopped"},
    {"name": "switch", "ip": "192.168.1.3", "status": "running"},
]

running_devices = list(filter(lambda device: device["status"] == "running", devices))
for device in running_devices:
    print(device["name"])

new_ips = list(map(lambda device: {"name": device["name"], "ip": device["ip"] + "/24"}, devices))

for device in new_ips:
    print(f"{device['name']} -> {device['ip']}")

# Explanation:
# 1. The `filter` function is used to extract devices with a "running" status.
#    - It filters the `devices` list based on the condition `device["status"] == "running"`.
#    - The result is stored in `running_devices`, which contains only the running devices.
#    - A loop then prints the names of these running devices.

# 2. The `map` function is used to add a "/24" subnet mask to the IP addresses of all devices.
#    - It creates a new dictionary for each device, appending "/24" to the `ip` field.
#    - The result is stored in `new_ips`, which contains the updated devices with modified IPs.
#    - A loop then prints the name and updated IP of each device.

def device_summary(components):
    running = 0
    stopped = 0
    for device in components:
        if device["status"] == "running":
            running += 1
        else:
            stopped += 1
    print(f"Total running devices: {running}")
    print(f"Total stopped devices: {stopped}")
    


components = [{"name": "Firewall", "ip": "192.168.1.1", "status": "running"},
    {"name": "router", "ip": "192.168.1.2", "status": "stopped"},
    {"name": "switch", "ip": "192.168.1.3", "status": "running"},
    {"name": "security", "ip": "192.168.1.4", "status": "running"}]

device_summary(components)

#---------------------------------------------------------------------------------

def analyze_devices(devices_new):
    running_firewalls = list(
        map(lambda device: device["name"],
            filter(lambda d: d["status"] == "running" and d["type"] == "Firewall", devices_new))
    )

    stopped_ips = list(
        map(lambda device: device["ip"],
            filter(lambda d: d["status"] == "stopped", devices_new))
    )

    return running_firewalls, stopped_ips


devices_new = [
    {"name": "FG1", "ip": "192.168.1.1", "status": "running", "type": "Firewall"},
    {"name": "R1", "ip": "192.168.1.2", "status": "stopped", "type": "Router"},
    {"name": "FG2", "ip": "192.168.1.3", "status": "running", "type": "Firewall"},
    {"name": "SW1", "ip": "192.168.1.4", "status": "stopped", "type": "Switch"}
]

running_firewalls, stopped_ips = analyze_devices(devices_new)

print("Running Firewalls:")
for firewall in running_firewalls:
    print(f"  {firewall}")

print("Stopped IPs:")
for ip in stopped_ips:
    print(f"  {ip}")
#---------------------------------------------------------------------------------
def summarize_devices(comps):
    # Filter running routers and stopped devices outside the loop
    Running_comps = list(filter(lambda d: d["status"] == "running" and d["type"]=="Router", comps))
    Stopped_ip = list(filter(lambda d: d["status"] == "stopped", comps))
    return Running_comps, Stopped_ip

comps = [
    {"name": "Router1", "ip": "10.0.0.1", "status": "running", "type": "Router"},
    {"name": "Firewall1", "ip": "10.0.0.2", "status": "stopped", "type": "Firewall"},
    {"name": "Router2", "ip": "10.0.0.3", "status": "stopped", "type": "Router"},
    {"name": "Router3", "ip": "10.0.0.4", "status": "running", "type": "Router"},
    {"name": "Switch1", "ip": "10.0.0.5", "status": "stopped", "type": "Switch"}
]

running_comps, stopped_ip = summarize_devices(comps)

print('Running router devices:')
for comp in running_comps:
    print(f"  {comp['name']})")

print('Stopped devices:')
for ip in stopped_ip:
    print(f"  ({ip['ip']})")

#---------------------------------------------------------------------------------
def special_devices(devs):
    running_devs = list(filter(lambda d: d["status"] == "running", devs))
    stopped_devs = list(filter(lambda d: d["status"] == "stopped", devs))
    return running_devs, stopped_devs

devs = [
    {"name": "Router1", "ip": "10.0.0.1", "status": "running", "type": "Router"},
    {"name": "Router2", "ip": "10.0.0.2", "status": "stopped", "type": "Router"},
    {"name": "Switch1", "ip": "10.0.0.3", "status": "running", "type": "Switch"},
    {"name": "Firewall1", "ip": "10.0.0.4", "status": "running", "type": "Firewall"},
    {"name": "Switch2", "ip": "10.0.0.5", "status": "stopped", "type": "Switch"}
]

running_devs, stopped_devs = special_devices(devs)

print("Running devices:")
for dev in running_devs:
    print(f"  {dev['type']}: {dev['name']}")

print("Stopped devices:")
for dev in stopped_devs:
    print(f"  {dev['ip']}")

print(f"\nTotal running devices: {len(running_devs)}")
print(f"Total stopped devices: {len(stopped_devs)}")