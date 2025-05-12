def device_info(**info):
    for k, v in info.items():
        print(f"{k} : {v}")

device_info(name="Router1", ip="10.0.0.1", model="ISR", status="running")

#----------------------------------------------------------------------------------------------

def show_firewall_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
show_firewall_info(name="FortiGate", ip="192.168.1.1", version="v7.0.5", status="running")

#the result will be:
# name : FortiGate
# ip : 192.168.1.1  
# version : v7.0.5
# status : running
# Explanation about **kwargs:
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# It collects these arguments into a dictionary, where the keys are the argument names 
# and the values are the argument values.

#-----------------------------------------------------------------------------------------------
def configure_device(**config):
    print("Configuring device with the following settings:")
    for key, value in config.items():
        print(f"{key} : {value}")
configure_device(
    name="FortiGate-01",
    type="Firewall",
    ip="192.168.1.1",
    status="running",
    port="WAN1",
    firmware="v7.2.1"
)
# the result will be:
# Configuring device with the following settings:
# name : FortiGate-01
# type : Firewall
# ip : 192.168.1.1
# status : running
# port : WAN1
# firmware : v7.2.1