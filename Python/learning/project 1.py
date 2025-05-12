# name= input("please enter your name: ")
# age= int(input("please enter your age: "))
# number= int(input("please enter your number: "))
# for i in range(1, 11):
#     print(f"{number} * {i} = {number*i}.")
#     i += 1
# total = 0    
# for i in range (1, 6):
    
#     total += i
# print(f"the sum of the numbers from 1 to 5 is {total} ")

dict1={'device1':('192.168.1.1','cisco','switch'),
       'device2':('192.168.1.2','fortigate','firewall'),'device3':('192.168.1.3','cisco','router')}
                  
allowed_ips = {'192.168.1.1','192.168.1.5','192.168.1.3'}

for device, details in dict1.items():  # Iterate over key-value pairs
    if details[0] in allowed_ips:  # Access the IP address from the value list
        print(f"{device} is allowed and running on IP {details[0]} and has a type of {details[2]}")
    else:
        print(f"{device} is either blocked or offline")

        