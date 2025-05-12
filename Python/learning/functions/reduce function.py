from functools import reduce

# نحسب مجموع أزمنة الاستجابة latency للأجهزة
devices = [
    {"name": "Firewall", "latency": 50},
    {"name": "Switch", "latency": 10},
    {"name": "Router", "latency": 100}
]


total_latency = reduce(lambda acc, device: acc + device["latency"], devices, 0)
# The `reduce` function is used to calculate the total latency of all devices.
# It takes three arguments:
# 1. A lambda function `lambda acc, device: acc + device["latency"]`:
#    - `acc` is the accumulator that stores the running total.
#    - `device["latency"]` is the latency of the current device being processed.
# 2. The `devices` list, which contains all the devices.
# 3. The initial value `0`:
#    - This is the starting value of the accumulator (`acc`).
#    - It ensures the summation starts from 0.
# The result is the total latency of all devices.

print(f"Total network latency is {total_latency} ms")