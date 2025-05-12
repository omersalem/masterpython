firewall = {"vendor": "fortinet", "version": "v7.2.1"}
security = {"status": "running", "model": "nexus 9300"}

firewall.update(security)
print(firewall)
#الشرح:

#update() تدمج محتويات قاموس آخر داخل قاموسك الحالي.
###إذا كان هناك مفتاح مشترك، يتم استبداله###

device1 = {"ip": "192.168.1.1", "vendor": "Cisco"}
device2 = device1.copy()

device2["ip"] = "192.168.1.2"

print(device1)
print(device2)
#الشرح:
#copy() تنسخ القاموس الحالي إلى قاموس جديد.
#الفرق بين copy() و update():
#copy() تنسخ القاموس الحالي إلى قاموس جديد.
#update() تدمج محتويات قاموس آخر داخل قاموسك الحالي.
#إذا كان هناك مفتاح مشترك، يتم استبداله

ports = {port: "open" for port in range(20, 26)}

print(ports)
#الشرح:
#dict comprehension
#إنشاء قاموس بطريقة مختصرة وسريعة باستخدام حلقة for داخل القاموس.
