class Sum:
    counter = 0 # Class Attribute

    @classmethod
    def class_method(cls):
        return f'This is a class method and the counter is {cls.counter}'
    @staticmethod
    def static_method():
        return f'This is a static method and the counter is {Sum.counter}'
    
    def __len__(self,a,b):
        # This method is used to return the length of the two numbers:
        print(f'The length of the two numbers is {len(str(a)) + len(str(b))}')
       
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'this message is from init magic method')

    def total(self):
        return self.a + self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        
        return self.a * self.b
    def modulus(self):
        return self.a % self.b
    def exponent(self):
        return self.a ** self.b
    def floor_division(self): 
        return self.a // self.b

group1 = Sum(1, 2)
print(f'{group1.a} + {group1.b} = {group1.total()}') #print(group1.total())
print(f'the sum of the two numers is  {group1.total()} and the division is {group1.division()} and the substraction is {group1.subtraction()} and the multiplication is {group1.multiplication()}\n and the modulus is {group1.modulus()} and the exponent is {group1.exponent()} and the floor division is {group1.floor_division()}')

print('*' * 50)

class hasLetterA:
    def __init__(self, name):
        self.name = name

    def check(self):
        for letter in self.name:
            if letter == 'a':
                return f'The letter a is in the name {self.name}'
                break
        else:
            return f'The letter a is not in the name {self.name}'
string1 = hasLetterA('ahmed')
print(string1.check())
print(Sum.class_method())
print(Sum.static_method())
group2= Sum(2,3)
#to call the len method we need to call the instance of the class
print(group2.__len__(2,3))

print("*" * 50)
class person:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
        print(f'the length of the person is {self.length} and the weight is {self.weight}')
    def characteristics(self):
        print(f'The length of the is person is {self.length} and the weight is {self.weight}')
class student(person):
    def __init__(self, length,weight, name, age,speed=0):
        super().__init__(length, weight)
        self.name = name
        self.age = age
        self.speed = speed
        print(f'the length of the student is {self.length} and the weight is {self.weight} and the name is {self.name} and the age is {self.age}')
    def speedy(self):
        s=int(input('please enter the speed of the student'))
        print(f'The speed of the student is {s}')
omar= student(1.75, 70, 'omar', 20) #here we didnt pass the speed so it will take the default value of 0
omar.characteristics()
omar.speedy()


      



