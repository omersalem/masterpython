# Initialize a list of devices
devices = ["fortigate", "cisco switch", "exchange", "ADS"]

# Print the first device in the list
print(devices[0])

# Print the last device in the list
print(devices[-1])

# Add a new device to the list
devices.append("Firewall FMC")

# Remove a specific device from the list
devices.remove("exchange")

# Print the updated list of devices
print(devices)

# Iterate through the list and print each device with a message
for i in devices:
    print(f"deivces in use are {i}")
