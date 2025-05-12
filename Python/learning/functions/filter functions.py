# نريد فقط الأجهزة العاملة "running"
devices = [
    {"name": "Firewall", "status": "running"},
    {"name": "Switch", "status": "stopped"},
    {"name": "Router", "status": "running"}
]

# The `filter` function is used to filter out devices based on their status.
# It applies the lambda function `lambda device: device["status"] == "running"` to each device in the `devices` list.
# Only devices where the status is "running" are included in the `running_devices` list.

running_devices = list(filter(lambda device: device["status"] == "running", devices))

for device in running_devices:
    print(device["name"])


