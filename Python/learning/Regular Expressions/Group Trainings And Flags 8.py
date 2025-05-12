# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)
# to explain the pattern:
# (https?) => Match "http" or "https"
# (www)? => Match "www" if it exists
# \.? => Match "." if it exists
# (\w+) => Match the domain name (alphanumeric characters)
# \.(\w+) => Match the top-level domain (like "com", "org", etc.)
# :?(\d+)? => Match the port number if it exists
# /?(.+) => Match the query string if it exists
# The search() function returns a match object if a match is found, otherwise it returns None

print(search.group()) # https://www.elzero.org:8080/category.php?article=105?name=how-to-do
print(search.groups()) # ('https', 'www', 'elzero', 'org', '8080', 'category.php?article=105?name=how-to-do')

for group in search.groups(): # Iterate through the matched groups

  print(group) # Print each matched group

print(f"Protocol: {search.group(1)}") # https
print(f"Sub Domain: {search.group(2)}") # www
print(f"Domain Name: {search.group(3)}") # elzero
print(f"Top Level Domain: {search.group(4)}") # org
print(f"Port: {search.group(5)}") # 8080
print(f"Query String: {search.group(6)}") # category.php?article=105?name=how-to-do
print(f"Full URL: {search.group(0)}") # https://www.elzero.org:8080/category.php?article=105?name=how-to-do

# Flags
# re.I => Ignore Case example: re.search(r"elzero", "ElZero", re.I)
# re.M => Multi Line example: re.search(r"^elzero", "ElZero\nElZero", re.M)
# re.S => Dot Matches New Line example: re.search(r"elzero.*", "ElZero\nElZero", re.S)
# re.X => Ignore Spaces And Comments example: re.search(r"""elzero
#  # This is a comment""", "ElZero # This is a comment", re.X)
