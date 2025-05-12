class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

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
