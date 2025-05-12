import arabic_reshaper
from bidi.algorithm import get_display
print("hello world")
n = input("please enter the name of you:\n")  # Write the name on a new line
print("your name is", n)
age = int(input("please enter your age: "))  # Ask for age and convert to integer
print("your age is", age)
print(type(age))
float(age)  # Convert age to float
print("your age is", age)   # Print the age again to show it is still an integer

name = input("ما اسمك؟\n")  # Ask for name in Arabic
age = int(input("كم عمرك؟ \n"))  # Ask for age in Arabic
reshaped_text = arabic_reshaper.reshape(f"مرحبا يا {name} عمرك هو {age}")
bidi_text = get_display(reshaped_text)
print(bidi_text)  # Print the reshaped and BiDi-corrected Arabic text