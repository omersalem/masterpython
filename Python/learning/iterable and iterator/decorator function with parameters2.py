# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    if num1 < 0 or num2 < 0: #here we can use decoration to check all the functions we want to cehck 
      #and this is very useful and we can make many tests on the functions

      print("Beware One Of The Numbers Is Less Than Zero")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

def myDecoratorTwo(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    print("Coming From Decorator Two")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator
@myDecoratorTwo #here we applied two decorators on the function

def calculate(n1, n2): 

  print(n1 + n2)

calculate(-5, 90) 


print("#" * 50)


def nohelloword(words):
  def nestedFunc(x):
    if x == 0:
      print("dont say 0")
      

      

    words(x)
  return nestedFunc
  

@nohelloword
def words(x):
  mywords = [x+1, x*2, x-4, x/2]
  for word in mywords:
    print(word)

words(0)




            