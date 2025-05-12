# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# so here if we want to split the string by space we can use split and in the ⁡⁢⁣⁣pattern⁡ we put ⁡⁢⁣⁣\s⁡ and in the
# ⁡⁢⁣⁣string⁡ we put the string we want to split and max split is the number of times we want to split
# to choose the number of times we want to split and we can remove the max split if we want to apply
# the split on all the string the split on all the string
# ---------------------------------------------------------------------


# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want And Return The New String
# so here if we want to replace space with - we can use sub and in the ⁡⁢⁣⁣pattern⁡ we put ⁡⁢⁣⁣\s⁡ and in the
# ⁡⁢⁣⁣replace⁡ we put the string we want to replace with and in the ⁡⁢⁣⁣string⁡ we put the string we want to add and replace count is the number of times we want to replace
# to choose the number of times we want to replace and we can remove the replace count if we want to apply
# the replace on all the string the replace on all the string
# ---------------------------------------------------------------------

import re

string_one = "I Love Python Programming Language" # This is a string with spaces

search_one = re.split(r"\s", string_one, 1) # Split the string into a list of words using space as the delimiter

print(search_one) # The result will be ['I', 'Love Python Programming Language'] because we used max split 1

print("#" * 50)

string_two = "How-To_Write_A_Very-Good-Article" # This is a string with - and _

search_two = re.split(r"-|_", string_two) # Split the string into a list of words using - and _ as delimiters
# The result will be ['How', 'To', 'Write', 'A', 'Very', 'Good', 'Article']

print(search_two) 

print("#" * 50)

# Get Words From URL

for counter, word in enumerate(search_two, 1): # Start from 1 and add no beside the each element in the list
  # Enumerate function is used to add a counter to the iterable and returns it in the form of an enumerate object

  if len(word) == 1: # If the length of the word is 1, skip it

    continue # Skip the word if its length is 1

  print(f"Word Number: {counter} => {word.lower()}") # Print the word number and the word in lowercase
# The result will be
# Word Number: 1 => how
# Word Number: 2 => to
# Word Number: 3 => write
# Word Number: 5 => very
# Word Number: 6 => good
# Word Number: 7 => article

print("#" * 50)

my_string = "I Love Python"

print(re.sub(r"\s", "-", my_string, 1)) # Replace the first space in the string with a hyphen (-)
# The result will be I-Love Python because we used max replace 1 and if we remove the max replace it will be
#  I-Love-Python