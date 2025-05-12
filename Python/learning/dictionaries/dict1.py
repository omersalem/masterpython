firewall={"vendor":"fortinet","version":"v7.0.5","ip":"192.168.1.1"}
firewall["status"]="Running"
firewall["version"]="v7.2.1"
print(firewall.values())
print(firewall.keys())
print(f"firewall from {firewall["vendor"]} with IP {firewall["ip"]} is running version {firewall["version"]}")
print(firewall.get("status"))