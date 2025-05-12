# *args: يسمح لك بتمرير عدد غير محدود من القيم إلى الدالة كـ 
# tuple، دون تحديد عددها مسبقًا.

def add_devices(*devices):
    for device in devices:
        print(f"Device added: {device}")

add_devices("Firewall", "Switch", "Router", "FMC")

#------------------------------------------------------------------------------------------------------
