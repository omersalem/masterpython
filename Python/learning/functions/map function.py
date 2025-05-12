# نريد تحويل جميع الآيبي إلى صيغة عليها "/24"
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

ips_with_mask = list(map(lambda ip: ip + "/24", ips))

print(ips_with_mask)
# الناتج: ['192.168.1.1/24', '10.0.0.1/24', '172.16.0.1/24']

# The `list` function is used here to convert the result of the `map` function (which is an iterator) 
# into a list.
# It ensures that the transformed IPs with "/24" are stored as a list that can be printed or reused.

