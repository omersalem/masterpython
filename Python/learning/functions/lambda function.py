# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function


def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"

hello = lambda name, age : f"Hello {name} your Age Is: {age}"

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))

print('*' * 50)
#------------------------------------------------------------------------------------------------------------



# دالة عادية
def add(x, y):
    return x + y

# باستخدام lambda
add = lambda x, y: x + y

print(add(5, 3))  # الناتج: 8
print('*' * 50)
#------------------------------------------------------------------------------------------------------------

devices = [
    {"name": "Firewall", "latency": 50},
    {"name": "Switch", "latency": 10},
    {"name": "Router", "latency": 100}
]

# ترتيب الأجهزة حسب زمن الاستجابة latency باستخدام lambda
devices_sorted = sorted(devices, key=lambda device: device["latency"])  # Fixed missing 'key' argument

for device in devices_sorted:
    print(f"{device['name']} latency: {device['latency']} ms")
#------------------------------------------------------------------------------------------------------------