from operator import le


class person:
    def __init__(self,name,age):

        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'Hello, your name is {self.name} and you are {self.age} years old.')

class student(person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
        pass
    def average(self):
        no_grades = int(input('enter the number of grades'))
        grades = []
        for i in range(no_grades):
            grade = int(input('enter the grade'))
            grades.append(grade)
        print(sum(grades))
        print(len(grades))
        average = sum(grades) / len(grades)
        if average >= 60:
            print(f'passed with average {average}.')
        else:
            print(f'failed with average {average} .')
    
class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        pass
    def teach(self):
        print(f'Teaching {self.subject}.')

student1 = student('John', 20)
teacher1 = teacher('Mr. Smith', 40, 'Math')
student1.average()
