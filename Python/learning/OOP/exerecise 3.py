class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

class engineer(Employee):
    def __init__(self, name , age ,salary, field):
        super().__init__(name, age, salary)
        self.field = field
    def develop(self):
        print(f"Developing in {self.field} field.")

omar=Employee('omar', 20, 2000)
ali=engineer('ali', 25, 3000, 'software')
ali.show_info()
ali.develop()

        