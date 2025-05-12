devices = [
    {"name": "FortiGate-1", "type": "Firewall", "ip": "192.168.1.1", "status": "open"},
    {"name": "CoreSwitch", "type": "Switch", "ip": "192.168.1.2", "status": "closed"},
    {"name": "router", "type": "Router", "ip": "192.168.1.3", "status": "closed"},
    {"name": "CoreSwitch2", "type": "Switch", "ip": "192.168.1.4", "status": "open"},
    {"name": "Router2", "type": "Router", "ip": "192.168.1.5", "status": "closed"}
]

for device in devices:
    if device['status'] == 'open':
        for key , value in device.items():
            print(f"{key} : {value}")
            print("-" * 30)
    else:
        print(f"{device['name']} is closed and we cannot access it")