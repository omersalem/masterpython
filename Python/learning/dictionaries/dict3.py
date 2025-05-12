firewall = {"vendor": "fortinet", "version": "v7.0.5", "ip": "192.168.1.1"}
firewall.update({"status": "Running"})
firewall.pop("ip")
firewall.setdefault('model', 'nexus 9300')
print(firewall.items())

for key, value in firewall.items():
    print(f"{key} : {value}")
# #the result of for loop is like this:
# # vendor : fortinet
# # version : v7.0.5
# # status : Running
# # model : nexus 9300

