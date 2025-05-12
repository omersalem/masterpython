def device_type_counter(type_name):
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(f"{type_name} count: {count}")

    return increment

firewall_counter = device_type_counter("Firewall")
firewall_counter()  # Firewall count: 1
firewall_counter()  # Firewall count: 2

router_counter = device_type_counter("Router")
router_counter() # Router count: 1

# # تعريف دالة رئيسية تأخذ نوع الجهاز كوسيط (مثل "Firewall" أو "Router")
# def device_type_counter(type_name):
#     count = 0  # تعريف عداد يبدأ من صفر

#     # تعريف دالة داخلية تقوم بزيادة العداد
#     def increment():
#         nonlocal count  # نستخدم المتغير count من المجال الخارجي (وليس إنشاء واحد جديد)
#         count += 1  # نزيد قيمة العداد بمقدار 1
#         print(f"{type_name} count: {count}")  # نطبع نوع الجهاز مع العدد الحالي

#     return increment  # نرجع الدالة الداخلية لتُستخدم لاحقًا

# # إنشاء عدّاد جديد لأجهزة "Firewall"
# firewall_counter = device_type_counter("Firewall")

# # استدعاء عدّاد الـ Firewall مرتين، كل مرة يزيد العداد ويطبع القيمة
# firewall_counter()  # الناتج: Firewall count: 1
# firewall_counter()  # الناتج: Firewall count: 2

# # إنشاء عدّاد جديد لأجهزة "Router"
# router_counter = device_type_counter("Router")

# # استدعاء عدّاد الـ Router مرة واحدة، يبدأ من صفر بشكل مستقل
# router_counter()  # الناتج: Router count: 1
# -----------------------------------------------------------------------------

# firewall_counter = device_type_counter("Firewall")
# تنشئ متغير count = 0.

# تنشئ دالة increment() داخلية.

# تُعيد الدالة increment() كنتيجة.

# الآن، firewall_counter أصبح يُشير إلى هذه الدالة increment().

# firewall_counter()
# تُنفذ الدالة increment().

# تزيد count بمقدار 1.

# تطبع "Firewall count: <القيمة>".

# وهكذا في كل مرة تنفذ firewall_counter()، يتم تنفيذ increment() وترتفع قيمة count داخل تلك الدالة المحفوظة في الذاكرة.

# #---------------------------------------------------------------------------------
# دالة خارجية تأخذ نوع الحالة (مثلاً: running أو stopped)
def create_status_tracker(status_type): 
    num = 0  # عداد خاص بكل نوع حالة

    # دالة داخلية تقوم بزيادة العداد وطباعة النتيجة
    def increment():
        nonlocal num  # نستخدم nonlocal حتى نعدل على المتغير num من الدالة الخارجية
        num += 1
        print(f"{status_type} devices count: {num}")

    return increment  # نُرجع الدالة الداخلية وليس ناتج تنفيذها

# ننشئ دالة تتعقب عدد الأجهزة ذات الحالة "running"
device_status = create_status_tracker("running")
device_status()  # النتيجة: running devices count: 1
device_status()  # النتيجة: running devices count: 2

# ننشئ دالة أخرى مستقلة تتعقب عدد الأجهزة ذات الحالة "stopped"
device_status2 = create_status_tracker("stopped")
device_status2()  # النتيجة: stopped devices count: 1
device_status2()  # النتيجة: stopped devices count: 2
