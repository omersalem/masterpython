def ping_device(ip, count=4):
    print(f"Pinging {ip} with {count} packets...")

ping_device("192.168.1.1")      # تستخدم القيمة الافتراضية 4
ping_device("10.0.0.1", 10) 
# تستخدم القيمة المخصصة 10
#---------------------------------------------------------------------------------------------------------
def check_status(name,status="running"):
    print(f"Device {name} is {status}")
check_status("Firewall")      # تستخدم القيمة الافتراضية "running"
check_status("Switch", "stopped") 
# تستخدم القيمة المخصصة "stopped"

# Explanation about default parameters:
# Default parameters in Python allow you to define a function with default values for one or more parameters.
# If the caller does not provide a value for a parameter with a default, the function uses the default value.
# This is useful for creating functions with optional arguments.
# Example:
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
# greet("Alice")          # Uses default greeting "Hello"
# greet("Bob", "Hi")      # Uses custom greeting "Hi"

