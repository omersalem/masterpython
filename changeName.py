import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import datetime
import subprocess
import socket
import logging
import os
import sys
from typing import List, Tuple
import json

class ADRenameManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("أداة إعادة تسمية أجهزة AD")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # متغيرات التحكم
        self.devices = []  # قائمة الأجهزة [(ip, new_name)]
        self.restart_cancelled = False
        self.restart_thread = None
        self.log_file = "ad_rename_log.txt"
        
        # إعداد نظام السجلات
        self.setup_logging()
        
        # إنشاء الواجهة
        self.create_widgets()
        
        # بدء مراقبة حالة إعادة التشغيل
        self.check_restart_status()
    
    def setup_logging(self):
        """إعداد نظام تسجيل العمليات"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def create_widgets(self):
        """إنشاء عناصر الواجهة الرسومية"""
        # الإطار الرئيسي
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # عنوان البرنامج
        title_label = ttk.Label(main_frame, text="أداة إعادة تسمية أجهزة Active Directory", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # قسم إدخال البيانات
        input_frame = ttk.LabelFrame(main_frame, text="إدخال بيانات الأجهزة", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # IP Address
        ttk.Label(input_frame, text="عنوان IP:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.ip_entry = ttk.Entry(input_frame, width=20)
        self.ip_entry.grid(row=0, column=1, padx=(0, 20))
        
        # New Name
        ttk.Label(input_frame, text="الاسم الجديد:").grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        self.name_entry = ttk.Entry(input_frame, width=20)
        self.name_entry.grid(row=0, column=3, padx=(0, 20))
        
        # أزرار إضافة وحذف
        ttk.Button(input_frame, text="إضافة جهاز", command=self.add_device).grid(row=0, column=4, padx=5)
        ttk.Button(input_frame, text="حذف محدد", command=self.remove_selected).grid(row=1, column=4, padx=5, pady=5)
        
        # قائمة الأجهزة
        devices_frame = ttk.LabelFrame(main_frame, text="قائمة الأجهزة المحددة", padding="10")
        devices_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # جدول الأجهزة
        columns = ("IP Address", "الاسم الجديد", "الحالة")
        self.devices_tree = ttk.Treeview(devices_frame, columns=columns, show="headings", height=8)
        
        for col in columns:
            self.devices_tree.heading(col, text=col)
            self.devices_tree.column(col, width=150)
        
        # شريط التمرير للجدول
        devices_scrollbar = ttk.Scrollbar(devices_frame, orient=tk.VERTICAL, command=self.devices_tree.yview)
        self.devices_tree.configure(yscrollcommand=devices_scrollbar.set)
        
        self.devices_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        devices_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # أزرار التحكم الرئيسية
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
        self.rename_btn = ttk.Button(control_frame, text="بدء إعادة التسمية", 
                                   command=self.start_rename_process, style="Accent.TButton")
        self.rename_btn.grid(row=0, column=0, padx=10)
        
        self.cancel_restart_btn = ttk.Button(control_frame, text="إلغاء إعادة التشغيل", 
                                           command=self.cancel_restart, state="disabled")
        self.cancel_restart_btn.grid(row=0, column=1, padx=10)
        
        ttk.Button(control_frame, text="مسح السجل", command=self.clear_log).grid(row=0, column=2, padx=10)
        
        # حالة البرنامج
        self.status_var = tk.StringVar(value="جاهز")
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        ttk.Label(status_frame, text="الحالة:").grid(row=0, column=0, sticky=tk.W)
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var, foreground="blue")
        self.status_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # منطقة عرض السجل
        log_frame = ttk.LabelFrame(main_frame, text="سجل العمليات", padding="10")
        log_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # تكوين التمدد
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        devices_frame.columnconfigure(0, weight=1)
        devices_frame.rowconfigure(0, weight=1)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
    
    def add_device(self):
        """إضافة جهاز جديد لقائمة الأجهزة"""
        ip = self.ip_entry.get().strip()
        name = self.name_entry.get().strip()
        
        if not ip or not name:
            messagebox.showerror("خطأ", "يرجى إدخال عنوان IP والاسم الجديد")
            return
        
        # التحقق من صحة IP
        if not self.validate_ip(ip):
            messagebox.showerror("خطأ", "عنوان IP غير صحيح")
            return
        
        # التحقق من عدم تكرار IP
        for device_ip, _ in self.devices:
            if device_ip == ip:
                messagebox.showerror("خطأ", "هذا العنوان موجود بالفعل")
                return
        
        # إضافة الجهاز
        self.devices.append((ip, name))
        self.devices_tree.insert("", "end", values=(ip, name, "في الانتظار"))
        
        # مسح الحقول
        self.ip_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        
        self.log_message(f"تم إضافة جهاز: {ip} -> {name}")
    
    def remove_selected(self):
        """حذف الجهاز المحدد من القائمة"""
        selected_item = self.devices_tree.selection()
        if not selected_item:
            messagebox.showwarning("تحذير", "يرجى تحديد جهاز لحذفه")
            return
        
        # الحصول على بيانات العنصر المحدد
        item_values = self.devices_tree.item(selected_item[0])['values']
        ip_to_remove = item_values[0]
        
        # حذف من القائمة
        self.devices = [(ip, name) for ip, name in self.devices if ip != ip_to_remove]
        
        # حذف من الجدول
        self.devices_tree.delete(selected_item[0])
        
        self.log_message(f"تم حذف جهاز: {ip_to_remove}")
    
    def validate_ip(self, ip):
        """التحقق من صحة عنوان IP"""
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    
    def check_device_connectivity(self, ip):
        """التحقق من الاتصال بالجهاز"""
        try:
            result = subprocess.run(['ping', '-n', '2', ip], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            return False
    
    def check_domain_membership(self, ip):
        """التحقق من انضمام الجهاز للدومين"""
        try:
            # استخدام PowerShell للتحقق من حالة الدومين
            ps_command = f"""
            $computer = Get-WmiObject -Class Win32_ComputerSystem -ComputerName {ip} -ErrorAction SilentlyContinue
            if ($computer -and $computer.PartOfDomain) {{
                Write-Output "DOMAIN_JOINED"
            }} else {{
                Write-Output "NOT_DOMAIN_JOINED"
            }}
            """
            
            result = subprocess.run(['powershell', '-Command', ps_command], 
                                  capture_output=True, text=True, timeout=15)
            return "DOMAIN_JOINED" in result.stdout
        except Exception:
            return False
    
    def rename_computer(self, ip, new_name):
        """إعادة تسمية الجهاز باستخدام PowerShell"""
        try:
            # أمر PowerShell لإعادة تسمية الجهاز
            ps_command = f"""
            try {{
                Rename-Computer -ComputerName {ip} -NewName {new_name} -Force -PassThru
                Write-Output "SUCCESS"
            }} catch {{
                Write-Output "ERROR: $($_.Exception.Message)"
            }}
            """
            
            result = subprocess.run(['powershell', '-Command', ps_command], 
                                  capture_output=True, text=True, timeout=30)
            
            if "SUCCESS" in result.stdout:
                return True, "تم بنجاح"
            else:
                error_msg = result.stdout.strip() if result.stdout else result.stderr.strip()
                return False, error_msg
                
        except Exception as e:
            return False, str(e)
    
    def start_rename_process(self):
        """بدء عملية إعادة التسمية"""
        if not self.devices:
            messagebox.showwarning("تحذير", "لا توجد أجهزة في القائمة")
            return
        
        # تأكيد البدء
        if not messagebox.askyesno("تأكيد", 
                                  f"هل تريد بدء إعادة تسمية {len(self.devices)} جهاز؟\n"
                                  "سيتم إعادة تشغيل الأجهزة في الساعة 7:00 مساءً"):
            return
        
        # تعطيل زر البدء
        self.rename_btn.configure(state="disabled")
        self.status_var.set("جاري المعالجة...")
        
        # بدء المعالجة في خيط منفصل
        threading.Thread(target=self.process_devices, daemon=True).start()
    
    def process_devices(self):
        """معالجة جميع الأجهزة"""
        success_count = 0
        
        for i, (ip, new_name) in enumerate(self.devices):
            try:
                # تحديث حالة الجهاز في الجدول
                self.update_device_status(ip, "جاري الفحص...")
                
                # التحقق من الاتصال
                if not self.check_device_connectivity(ip):
                    self.update_device_status(ip, "خطأ: غير متصل")
                    self.log_message(f"فشل الاتصال بالجهاز {ip}")
                    continue
                
                # التحقق من انضمام الدومين
                self.update_device_status(ip, "التحقق من الدومين...")
                if not self.check_domain_membership(ip):
                    self.update_device_status(ip, "خطأ: ليس في الدومين")
                    self.log_message(f"الجهاز {ip} غير منضم للدومين")
                    continue
                
                # إعادة التسمية
                self.update_device_status(ip, "جاري إعادة التسمية...")
                success, message = self.rename_computer(ip, new_name)
                
                if success:
                    self.update_device_status(ip, "تم بنجاح")
                    self.log_message(f"تم تغيير اسم الجهاز {ip} إلى {new_name}")
                    success_count += 1
                else:
                    self.update_device_status(ip, f"خطأ: {message}")
                    self.log_message(f"فشل في تغيير اسم الجهاز {ip}: {message}")
                    
            except Exception as e:
                self.update_device_status(ip, f"خطأ: {str(e)}")
                self.log_message(f"خطأ في معالجة الجهاز {ip}: {str(e)}")
        
        # إنهاء المعالجة
        self.root.after(0, self.finish_processing, success_count)
    
    def update_device_status(self, ip, status):
        """تحديث حالة الجهاز في الجدول"""
        def update():
            for item in self.devices_tree.get_children():
                values = self.devices_tree.item(item)['values']
                if values[0] == ip:
                    self.devices_tree.item(item, values=(values[0], values[1], status))
                    break
        
        self.root.after(0, update)
    
    def finish_processing(self, success_count):
        """إنهاء عملية المعالجة"""
        self.rename_btn.configure(state="normal")
        
        if success_count > 0:
            self.status_var.set(f"تم بنجاح تغيير أسماء {success_count} جهاز")
            self.log_message(f"انتهت العملية بنجاح. تم تغيير أسماء {success_count} من {len(self.devices)} جهاز")
            
            # بدء مراقبة إعادة التشغيل
            self.start_restart_monitoring()
        else:
            self.status_var.set("فشلت جميع العمليات")
            self.log_message("فشلت جميع عمليات إعادة التسمية")
    
    def start_restart_monitoring(self):
        """بدء مراقبة وقت إعادة التشغيل"""
        self.restart_cancelled = False
        self.cancel_restart_btn.configure(state="normal")
        
        # بدء خيط مراقبة إعادة التشغيل
        self.restart_thread = threading.Thread(target=self.monitor_restart_time, daemon=True)
        self.restart_thread.start()
    
    def monitor_restart_time(self):
        """مراقبة وقت إعادة التشغيل"""
        while not self.restart_cancelled:
            now = datetime.datetime.now()
            target_time = now.replace(hour=19, minute=0, second=0, microsecond=0)
            
            # إذا فات الوقت المحدد، تأجيل لليوم التالي
            if now >= target_time:
                target_time += datetime.timedelta(days=1)
            
            # التحقق من ساعات العمل (8 صباحاً - 3 مساءً)
            if 8 <= now.hour < 15:
                time_diff = target_time - now
                hours, remainder = divmod(time_diff.total_seconds(), 3600)
                minutes, _ = divmod(remainder, 60)
                
                status_msg = f"إعادة التشغيل خلال {int(hours)} ساعة و {int(minutes)} دقيقة"
                self.root.after(0, lambda: self.status_var.set(status_msg))
                
                # التحقق كل دقيقة
                time.sleep(60)
                
                # إذا حان الوقت
                if datetime.datetime.now() >= target_time:
                    self.root.after(0, self.execute_restart)
                    break
            else:
                # خارج ساعات العمل
                self.root.after(0, lambda: self.status_var.set("خارج ساعات العمل - لا يوجد إعادة تشغيل"))
                time.sleep(300)  # فحص كل 5 دقائق
    
    def execute_restart(self):
        """تنفيذ إعادة التشغيل"""
        if self.restart_cancelled:
            return
        
        # إشعار المستخدم
        response = messagebox.askyesno("إعادة التشغيل", 
                                     "حان وقت إعادة تشغيل الأجهزة.\n"
                                     "هل تريد المتابعة؟")
        
        if not response:
            self.cancel_restart()
            return
        
        self.status_var.set("جاري إعادة تشغيل الأجهزة...")
        self.log_message("بدء إعادة تشغيل الأجهزة")
        
        # إعادة تشغيل الأجهزة التي تم تغيير أسمائها بنجاح
        threading.Thread(target=self.restart_devices, daemon=True).start()
    
    def restart_devices(self):
        """إعادة تشغيل الأجهزة"""
        restarted_count = 0
        
        for item in self.devices_tree.get_children():
            values = self.devices_tree.item(item)['values']
            ip, name, status = values[0], values[1], values[2]
            
            if "تم بنجاح" in status:
                try:
                    # أمر إعادة التشغيل
                    subprocess.run(['shutdown', '/r', '/t', '60', '/m', f'\\\\{ip}', 
                                  '/c', 'إعادة تشغيل بعد تغيير اسم الجهاز'], 
                                 timeout=10)
                    restarted_count += 1
                    self.log_message(f"تم إرسال أمر إعادة التشغيل للجهاز {ip}")
                except Exception as e:
                    self.log_message(f"فشل في إعادة تشغيل الجهاز {ip}: {str(e)}")
        
        # تحديث الحالة
        final_msg = f"تم إرسال أوامر إعادة التشغيل لـ {restarted_count} جهاز"
        self.root.after(0, lambda: self.status_var.set(final_msg))
        self.root.after(0, lambda: self.log_message(final_msg))
        self.root.after(0, lambda: self.cancel_restart_btn.configure(state="disabled"))
    
    def cancel_restart(self):
        """إلغاء إعادة التشغيل"""
        self.restart_cancelled = True
        self.cancel_restart_btn.configure(state="disabled")
        self.status_var.set("تم إلغاء إعادة التشغيل")
        self.log_message("تم إلغاء إعادة التشغيل بواسطة المستخدم")
    
    def check_restart_status(self):
        """فحص حالة إعادة التشغيل بشكل دوري"""
        now = datetime.datetime.now()
        
        # عرض الوقت الحالي
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.root.title(f"أداة إعادة تسمية أجهزة AD - {time_str}")
        
        # إعادة الفحص كل ثانية
        self.root.after(1000, self.check_restart_status)
    
    def log_message(self, message):
        """إضافة رسالة لسجل العمليات"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # إضافة للسجل المرئي
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
        # إضافة لملف السجل
        self.logger.info(message)
    
    def clear_log(self):
        """مسح السجل المرئي"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("تم مسح السجل المرئي")
    
    def run(self):
        """تشغيل البرنامج"""
        self.log_message("تم بدء تشغيل برنامج إعادة تسمية أجهزة AD")
        self.log_message("ساعات العمل: 8:00 صباحاً - 3:00 مساءً")
        self.log_message("وقت إعادة التشغيل: 7:00 مساءً")
        self.root.mainloop()

if __name__ == "__main__":
    # التحقق من تشغيل البرنامج كمدير
    try:
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            messagebox.showerror("خطأ", "يجب تشغيل البرنامج كمدير (Run as Administrator)")
            sys.exit(1)
    except:
        pass
    
    # إنشاء وتشغيل التطبيق
    app = ADRenameManager()
    app.run()