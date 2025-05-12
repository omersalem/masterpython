firewall_info = {'vendor':'fortinet','ip':'192.168.1.1'}
security_info = {'model':'nexus 9000','status':'running'}
security_info.update(firewall_info)
security_info2 = security_info.copy()






security_info2['ip']='192.168.1.20'
for key , value in security_info.items():
    print(f"{key} : {value}")

                




for key , value in security_info2.items():
    print(f"{key} : {value}")


