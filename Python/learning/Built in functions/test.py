names = ['Alic e', 'Bo b', 'Char lie', 'Da vid', 'Eve']
new_names = list(map(lambda name: f'hello {name.replace(" ", "").upper()}', names))  # Replace spaces and convert to uppercase
for name in new_names:
    print(name)

#so capitalize make the first letter of the string uppercase 
# and upper make all the letters of the string uppercase and lower make all the letters of the string lowercase
# we used replace to remove the spaces in the string