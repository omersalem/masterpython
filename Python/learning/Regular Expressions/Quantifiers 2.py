    # ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more # this regular expression matches zero or more occurrences of the previous character
# +	1 or more # this regular expression matches one or more occurrences of the previous character
# ?	0 or 1 # this regular expression matches zero or one occurrence of the previous character
# {2}	Exactly 2 occurrences
# {2, 5}	Between 2 and 5 occurrences
# {2,}	2 or more occurrences
# (,5}	Up to 5 occurrences
# \w{3}	Exactly 3 word characters
# \w{3,}	At least 3 word characters or more
# \w{}	Any number of word characters
# \w{,3}	At most 3 word characters  
# \w{3,4}	Between 3 and 4 word characters
# \s       # this regular expression matches a single whitespace character
# \s{2}    # this regular expression matches two whitespace characters
# \S       # this regular expression matches a single non-whitespace character
# \d       # this regular expression matches a single digit
# \D       # this regular expression matches a single non-digit
#
# -------------
# w can be digits or word characters

# for example if want to make regular expression for this number 011 5456-820 we write this expression
# \d{3}\s\d{4}-\d{3}

# website called ⁡⁢⁣⁣regex101.com⁡ to test regular expressions and see how it works and test them 