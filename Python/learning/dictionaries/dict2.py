cisco={"vendor":"cisco","version":"v7","ip":"192.168.1.1","status":"running"}
print(cisco.get("model","Unknown"))
cisco["model"]="Nexus 9000"
for key in cisco:
    print(f"{key} : {cisco[key]}")

#another way to use for to print keys and values

for key, value in cisco.items():
    print(f"{key} : {value}")
#the result of for loop is like this:
# vendor : cisco
# version : v7
# ip : 192.168.1.1  
# status : running
# model : Nexus 9000
#the options of cisco functions are:
# 1. get
# 2. items
# 3. keys
# 4. values
# 5. pop
# 6. popitem
# 7. clear
# 8. update
# 9. copy
# 10. fromkeys
# 11. setdefault
# 12. del
# 13. dict
# 14. dict.items
# 15. dict.keys
# 16. dict.values
# 17. dict.pop
# 18. dict.popitem
# 19. dict.clear
# 20. dict.update
# 21. dict.copy
# 22. dict.fromkeys
# 23. dict.setdefault
# 24. dict.__getitem__
# 25. dict.__setitem__
# 26. dict.__delitem__
# 27. dict.__contains__
# 28. dict.__iter__
# 29. dict.__len__  
