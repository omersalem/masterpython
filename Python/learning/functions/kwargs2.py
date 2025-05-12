def add_device_config(**config):    
    print("Adding device configuration:")
    for key, value in config.items():
        print(f"{key} : {value}")
add_device_config(
    name="fortigate firewall",
    ip="192.168.1.1",
    status="running",
    model="FG-60F",
    version="v7.0.5",
    location="Data Center")

add_device_config(
    name="Cisco Switch",
    ip="192.168.1.2",
    status="stopped",
    model="Catalyst 9300",
    version="v16.9",
    location="Main Office")

add_device_config(
    name="Palo Alto Firewall",
    ip="192.168.1.3",
    status="running",
    model="PA-3220",
    version="v10.0",
    location="Branch Office",port=25)

#---------------------------------------------------------------------------------
def print_device_report(**devices):
    print("Device Report:")
    count = 0
    for key, value in devices.items():  # Corrected iteration over devices
        print(f"  {key}: {value}")
        if key == "status" and value == "running":  # Check if status is "running"
            count += 1
    print(f"Total running devices: {count}")

print_device_report(
    name="Cisco Router",
    ip="192.168.1.1",
    status="running",
    model="ISR 4000")

