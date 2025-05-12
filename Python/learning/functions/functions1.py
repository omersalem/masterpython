def show_Ip(ip):
    print(f'the ip address is {ip}')

ip = '192.168.1.1'
show_Ip(ip)

def show_device_info(device_type, IP):
    print(f'The device type is {device_type} and its IP address is {IP}')
    
show_device_info('firewall','192.168.1.1')
