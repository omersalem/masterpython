ports_status = {}
#أنشأنا قاموسًا فارغًا ports_status.
# إضافة البورتات المفتوحة
for port in range(20, 26):
    ports_status[port] = "open"

# إضافة البورتات المغلقة
for port in range(30, 36):
    ports_status[port] = "closed"

# طباعة الحالة لكل بورت
for port, status in ports_status.items():
    print(f"Port {port} is {status}")
    #النتيجة:
    # Port 20 is open
    # Port 21 is open
    # Port 22 is open
    # Port 23 is open
    # Port 24 is open
    # Port 25 is open
    # Port 30 is closed
    # Port 31 is closed
    # Port 32 is closed
    # Port 33 is closed
    # Port 34 is closed
    # Port 35 is closed

